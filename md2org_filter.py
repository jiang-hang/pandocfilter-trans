#!/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import json
import time
import re


from pandocfilters import toJSONFilter, Emph, Para, Str, stringify, Header , Strong, Plain, Link , Space

#during the md to org , the inline code 你好`hello world`世界
#is converted to 你好=hello world=世界 , but this format is not correctly
#converted to html, the right output should be
#     你好 =hello world= 世界
#while, this filter is to insert the prefix and suffix blank for the inline
#code

#the usage is:
#pandoc -f markdown -t org --filter ./md2org_filter.py -o tt.org ./tt.md

def transPara(key, value, format, meta):
      if key == 'Para':
          out= []
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
