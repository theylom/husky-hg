#!/usr/bin/env python
#
#tdog-husky

import re
import os, sys
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def validate(fileslist):
    print fileslist
    errors = False
    try:
        for line in fileslist:
            if line.find("shared-assets-ui-host") == -1:
                print "reviewing %s" % line
                filename = line.split('/')[-1]
                filePath = os.getcwd() + '/' + line.split("M ")[-1].replace('\n', '')
                if line.startswith('M') or line.startswith('A'):
                    if line.find("spec.js") != -1:
                        print bcolors.WARNING + ('Test file added/modified %s Running tests within that file.' % filename) + bcolors.ENDC
                        f=open(filePath, "r")
                        if f.mode == 'r':
                            contents =f.read()
                            m = re.search('describe\(\'(.+?)\', \(\) => \{', contents)
                            if m:
                                foundTestDescribe = m.group(1)
                                askExecuteTests = raw_input("Do you want to execute '%s' tests? (y/n): " % foundTestDescribe)
                                if askExecuteTests == 'y':
                                    try:
                                        subprocess.check_call('cd '+os.getcwd()+' && yarn karma start --grep "%s" --single-run' % foundTestDescribe, shell=True) == 0
                                    except (OSError, subprocess.CalledProcessError) as e:
                                        print  >> sys.stderr, str(e)
                                        errors = True
                    if line.find("index.js") != -1:
                        print '/'.join(filePath.split('/')[:-1]) + '/' + 'index.stories.js'
                        if os.path.exists('/'.join(filePath.split('/')[:-1]) + '/' + 'index.stories.js'):
                            print bcolors.WARNING + ('Component added/modified %s make sure you ran "yarn jest storybook -u" to create/update the snapshot.' % filename) + bcolors.ENDC
                    if line.find("stories.js") != -1:
                        print bcolors.WARNING + ('Stories file added/modified %s make sure you ran "yarn jest storybook -u" to create/update the snapshot.' % filename) + bcolors.ENDC
                if line.startswith('?'):
                    if line.find("stories.storyshot") != -1:
                        print bcolors.WARNING + ('Storyshot file created but was not added in the commit: %s.' % filename) + bcolors.ENDC

        if errors:
            print "Canceling commit due to errors found. Please check and fix."
            sys.exit(1)
        else:
            sys.exit(0)
    except Exception as e:
        print  >> sys.stderr, str(e)
if __name__ == '__main__':
    validate(os.popen('hg status'))