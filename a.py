#!/usr/bin/python3

import argparse

#parser = argparse.ArgumentParser()
parser2 = argparse.ArgumentParser()

parser.add_argument('topic', help='pleas set topic', type=str)

args = parser.parse_args()

if (args.topic) :
  print('topic={0}'.format(args.topic))

