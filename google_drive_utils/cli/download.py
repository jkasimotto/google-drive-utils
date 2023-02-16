import argparse
from google_drive_utils.download_files_from_folder.download import download_files
from google_drive_utils.cli.utils import add_common_args, parse_common_args


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--folder-id',
        help='The ID of the Google Drive folder to download files from'
    )
    parser.add_argument(
        '--dest-folder-path',
        help='The local path to save the downloaded files'
    )
    parser.add_argument(
        '--duplicate-options',
        help='How to handle duplicate files (overwrite, rename, skip, ask)'
    )

    add_common_args(parser)
    args = parser.parse_args()

    download_files(
        args.folder_id,
        args.dest_folder_path,
        args.duplicate_options,
        args.client_secret_path,
        args.token_path
    )


if __name__ == '__main__':
    main()
