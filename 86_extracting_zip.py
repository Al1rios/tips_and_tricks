
from zipfile import ZipFile

with ZipFile('Calotes.zip', 'r') as zipFile:
    print('printing the contents of the zip file')
    zipFile.printdir()
    # zipFile.extractall()