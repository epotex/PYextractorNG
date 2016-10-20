import os
try: # checking if the module installed
    from pyunpack import Archive as extractor
    from pytvdbapi import api
    import tmdbsimple as tmdb
except ImportError: #if module extption raised  exit
    print "Critical module not found, Please run pip install -r requirements.txt first!"
    exit()
import logging

###Variables ####
moviedb_api_key = "7fd4c0a5340d510450ca53c37925e5ba"
tvdb_api_key = "B43FF87DE395DF56"
log_file = "PYextractorNG.log"
logging.basicConfig(filename=log_file,level=logging.DEBUG, format='%(asctime)s %(message)s')
root_folder = "/Users/moshe_edri/Google Drive/tmp" # Config the root folder to start the scan from, Example:  "C:\" or "/tmp/
extentions = ['rar','zip'] # the extentions to look for, you can add more (7z, tar,gz, etc)
general_extract_path = "/general/"# Config the path to a general folder for extraction , Example:  "C:\" or "/tmp/
movie_extract_path = "/movie/"# Config the path to the movies folder, Example:  "C:\" or "/tmp/
tv_show_extract_path = "/tv_shows" #Config the path to the tv shows folder, Example:  "C:\" or "/tmp/
archive_dict = {}

def spider(folder):
    logging.info("Starting the scan in %s " % (folder))
    for folderName, subfolders, filenames in os.walk(folder):
        #print('The current folder is ' + folderName)
        for filename in filenames:
            file_ext = filename.split('.')[-1]
            if file_ext in extentions:
                logging.info("Found %s file: %s, Trying to categorized it... " % (file_ext.upper(), folderName + filename))
                categorized(filename)
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

def tvdb_search(tvshow):
    db = api.TVDB(tvdb_api_key)
    result = db.search(tvshow, 'en')
    if len(result) == 1:
        return True
    else:
        return False
def themoviedb_check(movie):
    tmdb.API_KEY = moviedb_api_key
    search = tmdb.Search()
    response = search.movie(query=movie)
    if response['total_results'] > 0:
        return True
    else:
        return False

def categorized(filename):
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
        logging.info("Couldn't categorized %s, the archive will be extracted to the general extract folder, adding it to the queue.  " % (filename))

spider(root_folder)