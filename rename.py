import sys
import os
from imdb import IMDb

root = "/data/videos/"

def stubrename(src, dest):
#    os.rename(src, dest)
#    print "renamed from " + src + " " + dest
    try:
        print "mv \"" + src + "\" \"" + dest + "\""
    except UnicodeEncodeError:
        pass

def getProperFileName(hint):
    ia = IMDb(accessSystem='http')
    results = ia.search_movie(hint, results=50)
#    i = 0
    return results[0]['long imdb title']
#    for movie in results:
#        print str(i) + " " + movie['long imdb title']
#        i = i+1
#
#        selection = input('What selection? ')
#        try:
#            return results[selection]['long imdb title']
#        except:
#            print None

for filename in os.listdir(root):
    try:
        f = filename.split('.')    
#        print f[0]
        newName = getProperFileName(f[0])
        if newName == None:
#            print "Couldn't find a new name for " + f[0]
            continue
        stubrename(root + filename, root + newName + "." + f[1])
    except IndexError:
#       print "Couldn't find a new name for " + f[0]
        continue
