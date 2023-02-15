import os

from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from tqdm import tqdm

from count import get_folder_file_count


def download_file(service, file_id, dest_path):
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
    file_count = get_folder_file_count(folder_id, service)

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
