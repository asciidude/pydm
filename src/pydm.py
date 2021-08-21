import requests
import os

gui = False

# CLI
if gui == False:
    url = requests.get('https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf')
    # url = requests.get(input('Input the DDL of your file: '))

    if not os.path.isdir(f'{os.getcwd()}/dl'):
        os.makedirs(f'{os.getcwd()}/dl')

    with open(f'{os.getcwd()}/dl/dummy_file.pdf', 'wb') as f:
        try:
            f.write(url.content)
        except:
            print("Unable to connect to server or download file from server")

# GUI
else:
    pass