import os
import requests
import argparse
import utils.str2bool
from clint.textui import progress

parser = argparse.ArgumentParser(description='A download manager')

parser.add_argument(
    'gui',
    nargs=1,
    metavar='gui',
    type=utils.str2bool.str2bool,
    help='Set if you want to use the GUI or not',
)

parser.add_argument(
    'link',
    nargs=1,
    metavar='link',
    type=str,
    help='Set the DDL link where the file will be downloaded',
)

parser.add_argument(
    'name',
    nargs=1,
    metavar='name',
    type=str,
    help='Set the name and extension of the file',
)

args = parser.parse_args()

# CLI
if args.gui[0] is False:
    if not os.path.isdir(f'{os.getcwd()}/dl'):
        os.makedirs(f'{os.getcwd()}/dl')

    req = requests.get(args.link[0], stream=True)

    with open(f'{os.getcwd()}/dl/{args.name[0]}', 'wb') as f:
        try:
            total_length = int(req.headers.get('content-length'))
        except requests.exceptions.InvalidHeader:
            print('[CONTACT DEVELOPER] Invalid header has been provided to download')

        if total_length is None:
            print('Unable to connect to server or download file from server')
        else:
            print(f'Downloading file {args.name[0]}')
            try:
                for chunk in progress.bar(
                    req.iter_content(chunk_size=1024),
                    expected_size=(total_length / 1024) + 1,
                ):
                    if chunk:
                        f.write(chunk)
                        f.flush()
                print('Download complete!')
            except requests.exceptions.InvalidURL:
                print('URL provided has been invalidated by the requests module')
# GUI
else:
    pass