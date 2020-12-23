# -*- coding: utf-8 -*-
from os import path as op
import sys, pysvn, os, time, datetime, shutil, subprocess

CUR_PATH = op.dirname(op.abspath(__file__))

def main():
    cnt = 1
    os.system('cls')
    os.system('python -m SimpleHTTPServer 8080')    


if __name__ == '__main__':
    print ('start web server:{}...'.format(CUR_PATH))
    os.chdir(CUR_PATH)
    main()
    print ('success, all done!')
    print ('success, press enter key to exit!')
    os.system('pause')
