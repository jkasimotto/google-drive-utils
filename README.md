# google-drive-api-utils

A collection of utilities for working with the Google Drive API. This package provides modules for counting things, downloading files from a Google Drive folder, and retrieving Google Drive credentials.

## Installation

You can install `google-drive-api-utils` using `pip`:

```python
pip install google-drive-api-utils
```

## Usage

### Counting things

The `count` module provides functions for counting things. To use it, simply import the module and call the `count` function:

```python
from google_drive_api_utils.count import count

numbers = [1, 2, 3, 4, 5]
count(numbers)  # Returns 5
```

### Downloading files from a Google Drive folder
The download module provides functions for downloading files from a Google Drive folder. To use it, you'll need to set up credentials for the Google Drive API (see below), then import the module and call the download_files function:
```python
from google_drive_api_utils.download.download_files_from_folder import download_files
import google.auth

# Authenticate with the Google Drive API
creds, _ = google.auth.default(scopes=['https://www.googleapis.com/auth/drive'])

# Download files from a Google Drive folder
folder_id = '1234567890'
dest_path = '/path/to/destination/folder'
download_files(creds, folder_id, dest_path)
```
The download_files function downloads all the files from the specified Google Drive folder and saves them to the specified destination folder.

The config.yaml file in the download directory contains options for handling duplicate files, such as overwriting existing files, renaming new files, skipping files, or prompting the user to decide what to do.

### Retrieving Google Drive credentials
The credentials module provides functions for retrieving Google Drive credentials. To use it, import the module and call the get_credentials function:
```python
from google_drive_api_utils.credentials.get_credentials import get_credentials

creds = get_credentials()
```
The get_credentials function retrieves the Google Drive credentials from a local file or prompts the user to authenticate and authorize the application if no credentials are found.

The config.yaml file in the credentials directory contains options for configuring the credentials file location and the OAuth scopes to use.

### License
This package is licensed under the MIT License. See the LICENSE file for details.