#!/bin/python3

import os
import glob
from distutils.dir_util import copy_tree
import sys
from datetime import datetime

def backup_script(target_dir, backup_dir):
  backup_dir = '{}/{}/{}/{}'.format(backup_dir, datetime.today().strftime('%Y_%m_%d'), datetime.today().strftime('%H_%M_%S'), target_dir)
  os.makedirs(backup_dir, exist_ok = True) 
  copy_tree(target_dir, backup_dir)


if __name__ == '__main__':
  backup_script(sys.argv[1], sys.argv[2])
