#!/usr/bin/python
import sys
import json
import re
import urllib2

# check if album is valid number
def validAlbum(album):
  try:
    num = int(album)
    if num < 1 or num > 100:
      print("%s is an invalid int value. Provide an int between 1 and 100." % num)
    return num
  except ValueError:
    print("Input: %s is of %s. Provide an int between 1 and 100" % (album, type(album)))
  except IndexError:
    print("Input: %s. Provide one int between 1 and 100" % album)

# ask user for album number
if len(sys.argv) > 2:
  sys.exit("Provide single int between 1 and 100")
else:
  album = sys.argv[1]

# validate user input
validAlbum(album)

# hit https://jsonplaceholder.typicode.com/photos >> query string: albumId=1-100
photos = urllib2.Request('https://jsonplaceholder.typicode.com/photos?albumId=%s' % album)
desc = urllib2.urlopen(photos,timeout=10).read()
jdata = json.loads(desc)

# print ALL photo ids and titles in album
for i in jdata:
  print "[%s] %s" % (i['id'], i['title'])
