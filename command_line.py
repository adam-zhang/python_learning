#!/usr/bin/python
#=============================================================================
#     FileName: command_line.py
#         Desc: 
#       Author: Mingping (Adam) Zhang
#        Email: mingpingzhang@163.com
#     HomePage: 
#      Version: 0.0.1
#   LastChange: 2015-08-19 10:06:03
#      History:
#=============================================================================

import sys

def main(argv):
    print "command:", argv[0]
    for i in range(1, len(argv)):
        print "argument ", argv[i]

if __name__ == "__main__":
    main(sys.argv)

