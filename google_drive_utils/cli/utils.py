import argparse

def add_common_args(parser):
    parser.add_argument('--client-secret-file', help='The path to the Google Drive API client secret file', default='client_secret.json')
    parser.add_argument('--token-file', help='The path to the Google Drive API token file', default='token.pickle')

def parse_common_args(args):
    return (args.client_secret_file, args.token_file)
