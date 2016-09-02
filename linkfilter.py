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


from pandocfilters import toJSONFilter, Emph, Para, Str, stringify, Header , Strong, Plain, Link, CodeBlock, Image

def transPara(key, value, format, meta):
      if key == 'Link':
          #print "Link"
          if debug == 1:
              fh.write("Link\n")
          hstr = stringify(value[1])
          hstr = re.sub(u"listing",u"清单",hstr)
          hstr = re.sub(u"figure",u"图",hstr)
          hstr = re.sub(u"table",u"表",hstr)
          hstr = re.sub("\.",u"-",hstr)
          if len(hstr) < 1:
            trStr=""
            return []
          elif re.match(u'图|表|清单[\d\-]+',hstr):
            return Str(hstr)
          elif re.match(u'[\d\-]+章',hstr):
            return Str(u"第"+hstr)
          elif re.match(u'第[\d\-]+章',hstr):
            return Str(hstr)
      elif key == "CodeBlock":
          v1=("",[],[])
          return CodeBlock(v1,value[1])
      elif key == "Image":
          v1=("",[],[])
          return Image(v1,value[1],value[2])
      else:
          return None

if __name__ == "__main__":
  toJSONFilter(transPara)
