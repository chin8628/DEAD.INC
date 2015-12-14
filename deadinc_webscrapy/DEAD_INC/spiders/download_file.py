import requests
def download_file(url):
    download = requests.get(url)
    fp = open("/var/www/DEAD_INC_downloaded/" + download.headers['Content-Disposition'][21:], "wb")
    fp.write(download.content)
    fp.close()
    print "Success! size:", download.headers['Content-Length'], "bytes"
