# PYextractorNG
I got tired extracting my archives manually :)

make sure you run "(sudo) pip install -r requirements.txt " first to install the python "patool" and "pyunpack" modules.

Important configurations to set:
1. 'root = "/" ' the folder where the scan start.
2. 'general_extract_path = "/tmp/"' the folder where the archive that couldn't be categorized will be extracted to.
3. 'movie_extract_path = "/tmp"'  archive that have been categorized as movies will be extracted to
4. 'tv_show_extract_path = "/tmp"'  archive that have been categorized as tv shows will be extracted to
5. 'moviedb_api_key = "7fd4c0a5340d510450ca53c37925e5bb"' create an account with tmdb in order to get a valid key
6. 'tvdb_api_key = "B43FF87DE395DF57"' create an account with tvdb in order to get a valid key


