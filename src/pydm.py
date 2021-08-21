import requests
import traceback
import os

# Testing
if not os.path.isdir(f'{os.path.abspath(__file__)}/dl'):
    os.makedirs(f'{os.path.abspath(__file__)}/dl', exist_ok=True)

url = requests.get('htstps://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf')

try:
    with open('dummy_file.pdf', 'wb') as f:
        f.write(url.content)
except:
    print(f'Failed to download file, error: {traceback.print_tb}')