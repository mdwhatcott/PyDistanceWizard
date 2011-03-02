from getpass import getpass
from datetime import date
from subprocess import Popen
from zipfile import ZipFile
import os

today = date.today()
download = "{0}{1}_commercial_csv.zip".format(today.strftime('%B')[:3], str(today.year))
file_to_extract = '5-digit Commercial.csv'
email = raw_input('Enter the username(email address) of the ZCD account: ')
password = getpass('Enter the password for the account: ')

url = "http://www.zipcodedownload.com/Account/Download/?file={0}&email={1}&password={2}"
formatted_url = url.format(download, email, password)
download_command = 'wget "{0}" --output-document={1}'.format(formatted_url, download)

print "Downloading the latest 5-digit database..."
process = Popen(download_command, shell=True)
process.wait()

archive = ZipFile(download, 'r')
print "Extracting the database file..."
archive.extract(file_to_extract)
archive.close()

os.remove(download)
print "Downloaded archive removed...Update complete."
