import os
try: # checking if the module installed
    from pyunpack import Archive as extractor
except ImportError: #if module extption raised  exit
    print "Critical module not found, Please run pip install -r requirements.txt first!"
    exit()
import logging
from pytvdbapi import api

moviedb_api_key = "a8b9f96dde091408a03cb4c78477bd14"
tvdb_api_key = "B43FF87DE395DF56"
log_file = "PYextractorNG.log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s %(message)s')
###Variables ####
root_folder = "/Users/moshe_edri/Google Drive/tmp" # Config the root folder to start the scan from, Example:  "C:\" or "/tmp/
rar_ext = "rar" # RAR extention
zip_ext = "zip" # zip extention
archive_dict = {}
general_extract_path = "/general/"# Config the path to a general folder for extraction , Example:  "C:\" or "/tmp/
movie_extract_path = "/movie/"# Config the path to the movies folder, Example:  "C:\" or "/tmp/
tv_show_extract_path = "/tv_shows" #Config the path to the tv shows folder, Example:  "C:\" or "/tmp/
def spider(folder):
    logging.info("Starting the scan in %s " % (folder))
    for folderName, subfolders, filenames in os.walk(folder):
        #print('The current folder is ' + folderName)
        for filename in filenames:
            if filename.split('.')[-1] == rar_ext:
                logging.info("Found rar file in: %s,Trying to categorise it... " % (folderName + filename))
                categorise(filename)
            if filename.split('.')[-1] == zip_ext:
                logging.info("Found zip file in: %s, Trying to categorise it... " % (folderName+filename))
                categorise(filename)
                #print('FILE INSIDE ' + folderName + ': '+ filename)
    if archive_dict.keys():
        logging.info("FINISHED, Found %s files to extract:"% (len(archive_dict)))
        for k, v in archive_dict.iteritems():
            extractor(k, v)
    else:
        logging.info("FINISHED the scan without finding archives to extract.")
    logging.info("FINISHED Extracting files")

def extractor(file, extract_path):

    logging.info("Extracting %s to %s" % (file, extract_path))

    #extractor("test.zip").extractall("/")

def themoviedb_check(movie):
    pass
def tvdb_search(tvshow):
    db = api.TVDB(tvdb_api_key)
    result = db.search(tvshow, 'en')
    if len(result) == 1:
        return True
    else:
        return False

def categorise(filename):
    logging.info("Checking TVDB if %s is a TV show... " % (filename))
    check = filename.split(".")[0]
    check = check.replace("_", " ")
    if tvdb_search(check):
        archive_dict[filename] = tv_show_extract_path
        logging.info("%s IS a TV show, and will be extracted to the TV show folder, adding it to the queue. " % (filename))
    elif themoviedb_check(check):
        logging.info("Checking THe Movie DB if %s is a movie... " % (filename))
        archive_dict[filename] = movie_extract_path
        logging.info("%s IS a Movie , and will be extracted to the Movie folder, adding it to the queue. " % (filename))
    else:
        archive_dict[filename] = general_extract_path
        logging.info("Couldn't categorise %s, the archive will be extracted to the general extract folder, adding it to the queue.  " % (filename))

spider(root_folder)