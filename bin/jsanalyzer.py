#!/usr/bin/env python3

"""
uifile_analyzer - convert a typescript into a python data structure for analysis
"""

import os
import datetime
import argparse
import pyjsparser

PARSER = argparse.ArgumentParser(description="""
Analyze .ts and .tsx files
""")

PARSER.add_argument("-i", metavar='<input>', dest='MY_INPUT', \
                    help="set source files or directories")

PARSER.add_argument("-o", metavar='<output>', dest='MY_OUTPUT', \
                    default='/var/tmp', help="set output dir")

PARSER.add_argument("-v", type=int, default=0, metavar='<verbose>', \
                    dest='VERBOSE', help="increase verbosity")

ARGS = PARSER.parse_args()

TODAY = datetime.datetime.today()
DSTAMP = TODAY.strftime("%Y%m%d")
TSTAMP = TODAY.strftime("%H%M%S")

def expand_target(target):
    """
    Walk a directory to find files
    """

    target_list = list()

    if os.path.isfile(target):
        target_list.append(target)

    if os.path.isdir(target):
        for rootdir, _directories, filenames in os.walk(target):
            for filename in filenames:
                target_list.append(os.path.join(rootdir, filename))

    return target_list

if __name__ == '__main__':

    for targetfile in expand_target(ARGS.MY_INPUT):
        print('FILE: {}'.format(targetfile))
        with open(targetfile, 'r') as targetfileobject:
            contents = targetfileobject.read()
            if ARGS.VERBOSE > 4:
                print('CONTENTS:\n {}'.format(contents))
            structure = pyjsparser.parse(contents)
            if ARGS.VERBOSE > 6:
                print('STRUCTURE:\n {}'.format(structure))
