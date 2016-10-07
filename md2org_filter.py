#!/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import json
import time
import re


debug=0

if debug == 1:
    fh = open("a.log","w")

from pandocfilters import toJSONFilter, Emph, Para, Str, stringify, Header , Strong, Plain, Link , Space

def transPara(key, value, format, meta):
      if key == 'Para':
          #print "Para"
          if debug == 1:
             fh.write("Para \n")
          out= []
          curstr=""
          for sv in value:
              if sv['t'] == "Code":
                  pre_space = Space()
                  suffix_space = Space()
                  out.append(pre_space)
                  out.append(sv)
                  out.append(suffix_space)
              else: #othe items , just keep them
                  out.append(sv)
          return Para(out)
      else:
          return None

if __name__ == "__main__":
  toJSONFilter(transPara)
