__author__ = 'marco'
from datetime import datetime
startTime = str(datetime.now())
import logging, zipfile, ftplib, configparser
errors = False

try:
    config = configparser.ConfigParser()
    config.read('config.ini')
    ftpData = config['ftp']
except PermissionError:
    print("could not access config file, permission denied")
    errors = True
except:
    print("could not access config file, does it exist?")
    errors = True

try:
    logging.basicConfig(filename="zipLog.txt", level=logging.DEBUG)
    logging.info("[" + startTime + '] Started script')
except PermissionError:
    print("Could not create error log, permission denied")
    errors = True
except:
    print("Unknown error, could not create logfile")
    errors = True


filename = datetime.now().strftime('%Y-%m-%d-%H-%M') + ".zip"

try:
    with zipfile.ZipFile(filename, 'w') as myzip:
        myzip.write('C:\zipFolder\dsffdsdsf.txt')
        myzip.write('C:\zipFolder\egGcf8e.png')
        myzip.write('C:\zipFolder\g2a-logo-300x300.png')
except PermissionError:
    print("Could not create ZIP due to write permission error")
    errors = True
except:
    print("unknown error, could not create ZIP file")
    errors = True

if not errors:
    try:
        ftpSession = ftplib.FTP(ftpData['hostname'], ftpData['username'], ftpData['password'])
        zipFile = open(filename, 'rb')
        ftpSession.storbinary('STOR ' + ftpData['targetFolder']+"/"+filename, zipFile)
        zipFile.close()
        ftpSession.quit()
    except ftplib.all_errors as e:
        print(str(e))





logging.info("[" + str(datetime.now()) + '] Script ended')