import click

from google_drive_utils.download.main import download


@click.command()
@click.option('--client-secret', type=click.Path(exists=True), help='Path to client secret JSON file')
@click.option('--folder-id', required=True, help='Google Drive folder ID to download files from')
@click.option('--to', default=None, help='Local directory to download files to')
@click.option('--max', type=int, default=None, help='Maximum number of files to download')
@click.option('--duplicate', default='skip', type=click.Choice(['skip', 'overwrite', 'rename']), help='How to handle duplicate filenames')
@click.option('--exclude', default=None, help='Comma-separated list of filenames to exclude from download')
@click.option('--mime-type', default=None, help='MIME type of files to download')
def download_cli(client_secret, folder_id, to, max, duplicate, exclude, mime_type):
    """
    Download files from a Google Drive folder using the Google Drive API.

    This command requires a client secret JSON file for authorization. You can obtain a client secret JSON file by creating a project in the Google Developers Console and configuring the OAuth 2.0 credentials.
    """
    if not client_secret:
        click.echo('Error: Client secret JSON file is required.')
        return

    download(client_secret, folder_id, to, max, duplicate, exclude, mime_type)


if __name__ == '__main__':
    download_cli()
