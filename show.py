#!/usr/bin/env python

import glob
import time
import argparse
import os

class Show:
  args = None

  def __init__(self):
    parser = argparse.ArgumentParser(description='Show computed ASCII image or gif.')
    parser.add_argument('-d', '--delay', nargs='?', default=0.07, type=float, help='delay between frames, default is 0.07 seconds.')
    parser.add_argument('folder', nargs='?', default='frames',type=str, help='folder containing the computed output.')

    self.args = parser.parse_args()
    

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
          print(content.read())
        if file_count == 1:
          return
        time.sleep(self.args.delay)

if __name__ == '__main__':
  show = Show()
  show.show()
