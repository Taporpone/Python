### Search through tpb with either clearnet or tor(default)
### Script is designed to scrap magnet links of torrents.
### To use tpb hs use torify i.e. torify python tpbscrapper.py
### Script is based on requests and BeautifulSoup

from bs4 import BeautifulSoup # handle requested sites
import requests # url requests


print('\nWelcome to tpbscrapper!')

def response_code_interpreter(request):
    http_responses = {200:"OK",400:"Bad Request",401:"Unauthorized",403:"Forbidden",404:"Not Found",408:"Request Timeout",500:"Internal Server Error",502:"Bad Gateway",503:"Service Unavailable",504:"Gateway Timeout"}

    try:
        return('%d %s') % (request.status_code,http_responses[request.status_code])
    except KeyError:
        return('%d (Response code not specified)') % (request.status_code)


# Script should by default connect using tor. If tor is not available or HS down script will default to clearnet

def login_screen():
    try:
        request = requests.get("http://uj3wazyk5u4hnvtk.onion/")
        if request.status_code == 200:
            base_url = 'http://uj3wazyk5u4hnvtk.onion/'
            print('\nTOR connection established!\n' + base_url + " <==> " + response_code_interpreter(request))
            return base_url
        else:
            base_url = 'https://thepiratebay.org/'
            print('\nTOR connection not established or HS down - defaulting to clearnet\n' +  base_url + " <==> " + response_code_interpreter(request))
            print response_code_interpreter(request)
            return base_url
    except:
        request = requests.get('https://thepiratebay.org/')
        base_url = 'https://thepiratebay.org/'
        print('\nTOR connection not established or HS down - defaulting to clearnet\n' +  base_url + " <==> " + response_code_interpreter(request))
        return base_url

base_url = login_screen()

### Search part
while True: #vaildate user's request, pass only if shorter than 150 chars.
    search_term = raw_input('\nPlease enter a phrase you would like to look for:\n> ')
    if len(search_term) > 150:
        print('Your search phrase is too long, there is a 150 char cap')
    else:
        break
#make url computer friendly
search_term = search_term.replace(' ','%20')
page = 0 ## set for future development of going thru pages
search_url = base_url + 'search/' + search_term + '/%d/7/' % page

#request search results
req = requests.get(search_url)

print search_url + " <==> " + response_code_interpreter(req)



soup = BeautifulSoup(req.content,'html.parser')

torrent_title = soup.find_all("tr") #Every torrent listed is in its own <tr></tr>

### Function created because I couldn't get Torrent Size to work with me because of non printable chars...
def size_print(item):
    size_raw = str(item.contents[3].find_all("font"))  #find piece of html with torrent size
    size_start = "Size" #Find in size_raw, this is where part we want starts
    size_end = "iB" #Find in size_raw, this is where it ends
    start = size_raw.find(size_start) #Where Size listing begins
    end = size_raw.find(size_end) #Where Size listing ends
    print_size = str(size_raw[start:end:]) #Get size_raw and print only Size info
    return print_size

#print found matches
for item in torrent_title:
    print item.contents[3].find_all("a")[0].text.replace("Name",'')
    print(size_print(item))
    print item.contents[3].find_all("a")[1].get("href")
    print('\n')
