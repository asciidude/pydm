import requests
from clint.textui import progress
import os

gui = False
req = None #requests.get('link', stream=True)

# CLI
if gui is False:
    # res = requests.get(input('Input the DDL of your file: '))
    file = input("What would you like your file to be named (example.js)? ")

    if not os.path.isdir(f'{os.getcwd()}/dl'):
        os.makedirs(f'{os.getcwd()}/dl')

    with open(f'{os.getcwd()}/dl/{file}', 'wb') as f:
        print(f"Downloading file {file}")
        try:
            total_length = int(req.headers.get('content-length'))
        except requests.exceptions.InvalidHeader:
            print("[CONTACT DEVELOPER] Invalid header has been provided to download")

        if total_length is None:
            print("Unable to connect to server or download file from server")
        else:
            try:
                for chunk in progress.bar(req.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                    if chunk:
                        f.write(chunk)
                        f.flush()
            except requests.exceptions.InvalidURL:
                print("URL provided has been invalidated by the requests module")

# GUI
else:
    pass