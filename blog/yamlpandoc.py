#!/usr/bin/python

import yaml
import sys
import fileinput
import subprocess

# pandoc command
pandoc = 'pandoc'

# pandoc title block
titleblock = ['title', 'author', 'date']

# pandoc arguments
args = [pandoc]

# files to read
files = []

# single-letter arguments with follow-up
followargs = ['f', 'r', 't', 'w', 'o', 'V', 'D', 'H', 'B', 'A', 'T', 'c']

# separate input files from pandoc arguments
readarg = False
for a in sys.argv[1:]:
    # check for arguments
    if (a[0] == '-') or readarg:
        # append to pandoc arguments
        args.append(a)
        
        # check if next item is part of the argument
        readarg = False if readarg else (a[1] in followargs)
    else:
        # append to list of files
        files.append(a)

# create fileinput object
input = fileinput.input(files)

# the front matter
frontmatter = ''

# the document
document = ''

# flag if reading front matter
readfront = False

# read front matter from input
for line in input:
    # ignore blank lines
    if not line.strip():
        document += line
        continue
    
    if readfront:
        # check for closing front matter tag
        if line.rstrip() == '---':
            # end reading front matter
            break
        else:
            # add to front matter
            frontmatter += line
    else:
        # check for opening front matter tag
        if line.rstrip() == '---':
            # begin reading front matter
            readfront = True
        else:
            # no front matter, start document 
            document += line
            break

# read rest of document from input
for line in input:
    document += line

# parse front matter into variables
vars = yaml.safe_load(frontmatter)

print "vars is %s" % vars
print "vars'type is %s" % type(vars)
# make sure front matter is a dict
#if not isinstance(vars, dict):
#    vars = {}

print "vars.keys is %r" % vars.keys()
# process vars

print "vars is %s" % vars
# add variables to pandoc arguments
for v in vars:
    args.append('--variable=%s:%s' % (v, vars[v]))

print "args is %s" % args
# run pandoc
proc = subprocess.Popen(args, stdin=subprocess.PIPE)

# send document to pandoc
proc.communicate(document)

# done