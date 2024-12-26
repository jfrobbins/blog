#!/usr/bin/env python
# Author: Jon Robbins
# License: GPL3+
# based on the idea from https://trisquel.info/en/wiki/how-convert-comic-book-archives-cbrcbr-cbz
# 
# This script recursively loops through directories below a starting point and converts all cbr file to cbz files
#
# requires:
#   - unrar
#   - zip/unzip
#
# gist: https://gist.github.com/jfrobbins/442a27f798219f78b3da
#
import os
import zipfile
from subprocess import call
import shutil

#DELETE_CBR_FILES = False
DELETE_CBR_FILES = True

def ensure_dir(f):
    d = os.path.dirname(f)
    print('dir:', d)
    if not os.path.exists(d):
        os.makedirs(d)
        print('created directory')
    else:
        print("dir exists")
    return d

def make_zipfile(output_filename, source_dir):
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zipf.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zipf.write(filename, arcname)

def buildFileList(path):
    list_of_files = []
    path = os.path.abspath(path)
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename[-4:] == '.cbr': 
                list_of_files.append(os.sep.join([dirpath, filename]))
    return list_of_files
    
if __name__ == '__main__':
    list_of_files = buildFileList("./")
    for f in list_of_files:                
        print("converting file: " + f)        
        tmpdir = os.path.join(os.path.dirname(f), f[:-4]) + os.path.sep   
        print("tmpdir: ",tmpdir)   
        
        outfile = os.path.dirname(tmpdir) + '.cbz'          
        
        ensure_dir(tmpdir) #create a tmp dir
        print("tmp dir created: ", tmpdir)
        
        print("unraring")
        call(["unrar", "x", f, tmpdir]) #unrar the file
        
        print("zipping the temp directory to file:", outfile)        
        #call(['zip','-r',os.path.dirname(tmpdir) + '.cbz', tmpdir])
        make_zipfile(outfile, tmpdir)
        
        print("deleting the tmp directory")
        shutil.rmtree(tmpdir)
        
        if DELETE_CBR_FILES and os.path.isfile(outfile):
            print("deleting original cbr file: ", f)
            os.remove(f)
            
    print("done converting files")
    
