import os
try:
    from pyunpack import Archive as extractor
except ImportError:
    print "Critical module not found, Please run pip install -r requirements.txt first!"
import logging
log_file = "PYextractorNG.log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s %(message)s')
###Variables ####
root = "/" # Config the root folder to start the scan from, Example:  "C:\" or "/tmp/
rar_ext = "rar" # RAR extention
zip_ext = "zip" # zip extention
archive_list = []
extract_path = "/tmp/"# Config the path to the extracted folder, Example:  "C:\" or "/tmp/

def spider(folder):
    logging.info("Starting the scan in %s " % (folder))
    for folderName, subfolders, filenames in os.walk(folder):
        #print('The current folder is ' + folderName)
        for filename in filenames:
            if filename.split('.')[-1] == rar_ext:
                logging.info("Found rar file in: %s adding it to the queue" % (folderName+filename))
                archive_list.append(folderName+filename)
            if filename.split('.')[-1] == zip_ext:
                logging.info("Found zip file in: %s adding it to the queue" % (folderName+filename))
                archive_list.append(folderName+filename)
                #print('FILE INSIDE ' + folderName + ': '+ filename)
    if len(archive_list) != 0:
        logging.info("FINISHED, Found files to extract:")
        extractor(archive_list)
    else:
        logging.info("FINISHED the scan without finding archives to extract.")

def extractor(list):
    for file in list:
        logging.info("Extracting %s" % (file))
        extractor(file).extractall(extract_path)
    logging.info("FINISHED Extracting files)

spider(root)