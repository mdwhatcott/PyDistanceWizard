from datetime import date
from subprocess import call
from zipfile import ZipFile
import os

today = date.today()
download = "ca_{0}{1}_commercial_csv.zip".format(today.strftime('%B')[:3], str(today.year))
email = raw_input('Enter the username(email address) of the ZCD account: ')
password = raw_input('Enter the password: ')

url = "http://www.zipcodedownload.com/Account/Download/?file={0}&email={1}&password={2}"
formatted_url = url.format(download, email, password)
download_command = 'wget "{0}" --output-document={1}'.format(formatted_url, download)

print "Downloading the latest 6-digit database..."
response = call(download_command)

with ZipFile(download, 'r') as archive:
    print "Extracting the database file..."
    archive.extract('6-digit Commercial.csv')

os.remove(download)
print "Downloaded archive removed...Update complete."
