### Simple script for loading a torrent with more trackers.
###
### Logic: Take a hash, remove white spaces, send it to http://itorrents.org/torrent/hash.torrent and download torrent file.
### Usage: |python script.py hash| or |python script.py| if you want to manualy paste hash
### or |python script.py list.txt| to download multiple torrents from the list.
### List should be a single hash per line without spaces.

import sys
import requests

provider = "http://itorrents.org/torrent/"

def input_screen():
    tor_hash = raw_input("Please paste torrent's hash\n> ")
    tor_hash = tor_hash.replace(" ","") # Get rid of spaces
    return tor_hash

def download_torrent(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    if r.status_code != 200:
        print "Torrent not found :("
    else:
        with open(local_filename,"wb") as output:
            output.write(r.content)

def parse_list():
    hash_list = []
    with open("list.txt") as hash_lst:
        for line in hash_lst.readlines():
            hash_list.append(line.replace("\n",""))
    return hash_list

if sys.argv[-1] == "list.txt":    # If list of hashes
    hash_list = parse_list()
    print "# of hashes: " + str(len(hash_list))
    item_no = 1     # for printing current hash no
    for item in hash_list:
        base_url = provider + "%s.torrent" % item
        download_torrent(base_url)
        print "Processed %d/%d" %(item_no,len(hash_list))
        item_no += 1

elif len(sys.argv) == 2:        # if one hash with no spaces
    tor_hash = sys.argv[1]
    base_url = provider + "%s.torrent" % tor_hash
    download_torrent(base_url)

elif len(sys.argv) > 2:     # If more than 1 passed we assume there are spaces in hash, get rid of em
    tor_hash = "".join(sys.argv[1:])
    base_url = provider + "%s.torrent" % tor_hash
    download_torrent(base_url)
else:       # User will provide hash
    tor_hash = input_screen()
    base_url = provider + "%s.torrent" % tor_hash
    download_torrent(base_url)
