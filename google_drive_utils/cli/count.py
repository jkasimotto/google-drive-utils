import argparse
from google_drive_utils.count.count import count_files
from google_drive_utils.cli.utils import add_common_args


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--folder-id', help='The ID of the Google Drive folder to count files in', required=True)
    add_common_args(parser)
    args = parser.parse_args()

    count = count_files(args.folder_id, args.client_secret_file, args.token_file)
    print(f"Number of files in folder {args.folder_id}: {count}")


if __name__ == '__main__':
    main()
