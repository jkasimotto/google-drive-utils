import os

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from tqdm import tqdm
import yaml

from google_drive_utils.count.count import count_files

def read_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        return config['options']


def handle_duplicate_file(dest_file_path, options):
    if options['skip']:
        print(f"Skipping file '{dest_file_path}' because it already exists.")
        return False
    elif options['rename']:
        # Rename the file with a unique identifier
        filename, ext = os.path.splitext(dest_file_path)
        i = 1
        while os.path.exists(dest_file_path):
            dest_file_path = f"{filename}_{i}{ext}"
            i += 1
    elif options['ask']:
        # Ask the user what to do
        while True:
            choice = input(
                f"A file with the name '{dest_file_path}' already exists. What would you like to do? (o)verwrite, (r)ename, or (s)kip? ").lower()
            if choice == 'o':
                return True
            elif choice == 'r':
                # Rename the file with a unique identifier
                filename, ext = os.path.splitext(dest_file_path)
                i = 1
                while os.path.exists(dest_file_path):
                    dest_file_path = f"{filename}_{i}{ext}"
                    i += 1
                return True
            elif choice == 's':
                print(f"Skipping file '{dest_file_path}'.")
                return False
            else:
                print("Invalid choice. Please enter 'o', 'r', or 's'.")
    # Default behavior is to overwrite the file
    return True


def download_file(service, file_id, dest_path, options):
    # Check if a file with the same name already exists
    if os.path.exists(dest_path):
        should_download = handle_duplicate_file(dest_path, options)
        if not should_download:
            return False

    # Download the file
    request = service.files().get_media(fileId=file_id)
    with open(dest_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while done is False:
            try:
                status, done = downloader.next_chunk()
                print(f"Downloaded {int(status.progress() * 100)}.")
            except HttpError as error:
                print(f'An error occurred while downloading the file: {error}')
                return False

    return True


def download_files(service, folder_id, dest_path):
    # Get the number of files in the folder
    file_count = count_files(folder_id, service)

    if file_count is None:
        print('Exiting script due to an error.')
        return

    # Construct a progress bar
    pbar = tqdm(total=file_count, desc='Downloading files')

    # Construct the query to retrieve files in the folder
    query = f"'{folder_id}' in parents and trashed = false"

    try:
        # Send the request to the Drive API and get the list of files
        response = service.files().list(
            q=query, fields='nextPageToken, files(id, name)').execute()
        files = response.get('files', [])
    except HttpError as error:
        print(f'An error occurred while retrieving the list of files: {error}')
        print('Exiting script due to an error.')
        return

    # Loop through the list of files and download them
    for file in tqdm(files, desc='Downloading files'):
        # Download the file to the destination folder
        dest_file_path = os.path.join(dest_path, file['name'])
        success = download_file(service, file['id'], dest_file_path)
        if success:
            print(f"Downloaded {file['name']}.")
            # Update the progress bar
            pbar.update(1)
        else:
            print(f"Failed to download {file['name']}.")
            # We will continue trying to download the other files

    pbar.close()
    print('Download completed.')
