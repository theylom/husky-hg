#!/usr/bin/env python
#
#tdog-husky

import re
import os, sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def trailing_whitespace(fileslist):

    for line in fileslist:
        filename = line.split('/')[-1]
        if line.startswith('M'):
            print bcolors.WARNING + ('File modified %s' % filename) + bcolors.ENDC

if __name__ == '__main__':

    trailing_whitespace(os.popen('hg status'))
    sys.exit(1)