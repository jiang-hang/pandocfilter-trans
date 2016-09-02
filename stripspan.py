#!/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import json
import time
import re


debug=1

if debug == 1:
    fh = open("a.log","w")


from pandocfilters import toJSONFilter, Emph, Para, Str, stringify, Header , Strong, Plain, Link, CodeBlock, Image


top= 241 
bottom=-1

def dropHeaderFooter(style):
    #scan the style
    if style[0]:
        if style[0][0] == "style":
            rstyle = style[0][1]
            atts=re.split("; ",rstyle)
            s_top=re.search("top:(\d+)px",rstyle)
            s_bottom=re.search("height:(\d+)px",rstyle)
            if s_top :
                s_top = int(s_top.group(1))
            else:
                s_top = -1
            if s_bottom and s_top != -1:
                s_bottom = s_top + int(s_bottom.group(1))
            else:
                s_bottom = -1

            if debug == 1:
                fh.write("%s top:%d bottom %d\n"%(rstyle,s_top,s_bottom))
            if s_bottom != -1 and top != -1:
                if s_bottom < top :
                    return True
                else:
                    return False

            if s_top != -1 and bottom != -1:
                if s_top > bottom :
                    return True
                else:
                    return False
    return False

def transPara(key, value, format, meta):
      if key == 'Span':
          if dropHeaderFooter(value[0][2]):
              return []
          hstr = stringify(value[1])
          return Str(hstr)
      elif key == 'Div':
          if dropHeaderFooter(value[0][2]):
              return []
          hstr = stringify(value[1])
          if len(hstr) < 1:
            trStr=""
            return []
          return value[1]
      else:
          return None

if __name__ == "__main__":
  toJSONFilter(transPara)
