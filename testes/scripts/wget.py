#!/bin/env python3

import os, sys
from urllib.request import urlretrieve

def reporthook(blocknum, blocksize, totalsize):
    readsofar = blocknum * blocksize
    if totalsize > 0:
        percent = readsofar * 100 / totalsize
        if percent >= 100.0: # Near the end
            sys.stdout.write("\n")
            return
        s = "\rProgress: {0:.1f}% [{1}{2}] {3} / {4}".format(percent, "#"*int(percent//2), "."*int(50-(percent//2)), readsofar, totalsize)
        sys.stdout.write(s)
        
    else: # total size is unknown
        sys.stdout.write("read {}\n".format(readsofar))
        
for link in sys.argv[1:]:
    print("\nDownloading {}:".format(link)) 
    urlretrieve(link, os.path.basename(link), reporthook)