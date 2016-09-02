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


from pandocfilters import toJSONFilter, Emph, Para, Str, stringify, Header , Strong, Plain, Link

def rep(v):
   tt={}
   tt['t']="Str"
   tt['c']=re.sub(u"。"," ",v)
   return [tt]

def transPara(key, value, format, meta):
      if key == 'Header':
          if debug == 1:
              fh.write("Header\n")
          lev = value[0]
          newlev = 0
          if lev == 2 :
              newlev = 1
          elif lev == 3:
              newlev = 2
          elif lev == 4:
              newlev = 3
          elif lev >= 5:
              newlev = 5
	  if newlev == 5:
              v2=rep(stringify(value[2]))
              v2[0]['c']=re.sub(u"\.","-",v2[0]['c'])
              return Para([Strong(v2)])
          else:
              tt=("",[],[])
              v2=rep(stringify(value[2]))
              return Header(newlev,tt,v2)
      #elif key == 'Link':
      #    #print "Link"
      #    if debug == 1:
      #        fh.write("Link\n")
      #    hstr = stringify(value)
      #    trStr=""
      #    if len(hstr) < 1:
      #      trStr=""
      #      return []
      #    else:
      #      trStr=transWrapper(hstr,"Link")
      #    return Link(value[0],[Str(trStr)],value[2])
      else:
          return None

if __name__ == "__main__":
  toJSONFilter(transPara)
