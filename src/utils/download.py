from clint.textui import progress
import requests
import os

def download(dl_lnk, name, *args, **kwargs):
    req = requests.get(dl_lnk, stream=True)

    with open(f'{os.getcwd()}/dl/{name}' if kwargs.get("gui") is False else f'{os.getcwd()}/dl/{name}', 'wb') as f:
        total_length = int(req.headers.get('Content-Length'))

        if total_length is None:
            print('Unable to connect to server or download file from server')

        else:
            print(f'Downloading file {name}')
            try:
                for chunk in progress.bar(
                    req.iter_content(chunk_size=1024),
                    expected_size=(total_length / 1024) + 1,
                ):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if chunk:
                        f.write(chunk)
                        f.flush()
                    print('Download complete!')
            except requests.exceptions.InvalidURL:
                print('URL provided has been invalidated by the requests module')