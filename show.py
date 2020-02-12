#!/usr/bin/env python

import glob
import time
import argparse
import os

class colours:
  NONE = ''
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  ENDC = '\033[0m'

  get = {'': '', 
         'BLUE': '\033[94m',
         'GREEN': '\033[92m',
         'RED': '\033[91m',
         'YELLOW': '\033[93m'}

class Show:
  args = None
  startc = ''
  endc = ''

  def __init__(self):
    parser = argparse.ArgumentParser(description='Show computed ASCII image or gif.')
    parser.add_argument('-d', '--delay', metavar='f', nargs='?', default=0.07, type=float, help='delay between frames, default is 0.07 seconds.')
    parser.add_argument('folder', nargs='?', default='frames',type=str, help='folder containing the computed output.')
    parser.add_argument('-c', '--colour', nargs='?', default='', choices=['BLUE', 'GREEN', 'YELLOW', 'RED'], type=str)

    self.args = parser.parse_args()
    self.startc = colours.get[self.args.colour]
    if self.startc != '':
      self.endc = colours.ENDC
    

  def clear_screen(self):
    print("\033[H\033[J")

  def show(self):
    file_count = sum([len(files) for r, d, files in os.walk(self.args.folder)])
    while True:
      files = glob.glob(self.args.folder + '/*')
      files.sort(key = lambda x: float(x.strip(self.args.folder + '/output')))

      for f in files:
        with open(f, 'r') as content:
          self.clear_screen()
          print(self.startc + content.read() + self.endc)
        if file_count == 1:
          return
        time.sleep(self.args.delay)

if __name__ == '__main__':
  show = Show()
  show.show()
