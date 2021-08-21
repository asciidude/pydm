import requests
import traceback
import os

gui = False

if gui == False:
    url = requests.get('htstps://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf')
    # url = requests.get(input('Input the DDL of your file: '))

    try:
        with open(f'{os.path.abspath(__file__)}/dummy_file.pdf', 'wb') as f:
            f.write(url.content)
    except:
        print("Unable to connect to server or download file from server")
else:
    pass