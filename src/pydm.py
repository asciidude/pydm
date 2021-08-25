import os
import argparse
import utils.str2bool
import utils.download
from gui import main

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
    help='Set the name and extension of the file'
)

args = parser.parse_args()
dev_mode = True
gui = args.gui[0]

if __name__ == '__main__':
    # CLI
    if gui is False:
        if not os.path.isdir(f'{os.getcwd()}/dl'):
            os.makedirs(f'{os.getcwd()}/dl')

        utils.download.download()
    # GUI
    else:
        if dev_mode is True:
            main.show_main()