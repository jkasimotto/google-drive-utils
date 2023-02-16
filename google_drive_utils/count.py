
from googleapiclient.errors import HttpError

def get_folder_file_count(folder_id, service):
    # Construct the query to retrieve files in the folder
    query = f"'{folder_id}' in parents and trashed = false"

    # Send the request to the Drive API and get the number of files
    try:
        response = service.files().list(q=query, fields='nextPageToken, files(id)').execute()
        file_count = len(response['files'])

        # If there are more files, paginate through them to get the total count
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.files().list(q=query, fields='nextPageToken, files(id)',
                                            pageToken=page_token).execute()
            files = response.get('files', [])
            file_count += len(files)

        return file_count
    except HttpError as error:
        print(f'An error occurred while retrieving the number of files: {error}')
        return None
