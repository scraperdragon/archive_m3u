import requests,urllib,json,os,cgi
print ("#EXTM3U")
print ("# Created by Dragon Dave: github.com/scraperdragon twitter.com/dragondave")

# TODO: deal with multiple files [M3U? MP3 ZIP?]
# TODO: make default search not include erroneous modern music

formatlist=[u'Ogg Vorbis', u'160Kbps MP3',u'VBR MP3', u'128Kbps MP3',u'Flac',u'96Kbps MP3',u'64Kbps MP3',u'Windows Media Audio',u'Unknown']
def parsesearch(query="q=date%3A%5B1900-01-01+TO+1909-12-31%5D+AND+mediatype%3Aaudio"):
    baseurl="http://www.archive.org/advancedsearch.php?"
    suffix="&sort%5B%5D=&sort%5B%5D=&sort%5B%5D=&rows=9999&page=1&output=json&save=yes"
    r=requests.get(baseurl+query+suffix)
    j=json.loads(r.text)
    for d in j['response']['docs']:
        found=False
        identifier=d['identifier']
        formats=d['format']
        for f in formatlist:
            if f in formats:
                try:
                    c=d['creator'][0]
                except:
                    c="Unknown"
                try:
                    t=d['title']
                except:
                    t="Unknown"
                print ('#EXTINF:0, %s - %s'%(c,t))
                print ('http://www.archive.org/download/%s/format=%s' % (identifier,urllib.parse.quote_plus(f)))
                found=True
                break

parsesearch()

