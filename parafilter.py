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

def transLink(qq):
    qq = re.sub("listing",u"清单",qq)
    qq = re.sub("figure",u"图",qq)
    qq = re.sub("table",u"表",qq)
    return qq

def transHeader(qq):
    qq = re.sub(u"。",u" ",qq)
    return qq

#the default trans
def transCommon(qq):
    return qq

def trans(qq,context): 
    if context == "Link":
        qq=transLink(qq)
    if context == "Header":
        qq=transHeader(qq)
    qq=transCommon(qq)
    return qq

def transWrapper(content, context="Para"):
    #return '@B%sE@'%content
    if debug == 1:
        fh.write('@B%sE@'%content)
    #time.sleep(0.2)
    #print content
    res = trans(content,context)
    return res


from pandocfilters import toJSONFilter, Emph, Para, Str, stringify, Header , Strong, Plain, Link

def transPara(key, value, format, meta):
      if key == 'Para'  or key == 'Plain':
          #print "Para"
          if debug == 1:
             fh.write("Para \n")
          out= []
          curstr=""
          for sv in value:
              #print "processing...", sv
              if sv['t'] == "Str":
                  curstr = curstr + sv['c'] 
                  if debug == 1:
                      fh.write("out %s\n"%curstr)
              elif sv['t'] == "Space" or sv['t'] == "SoftBreak" or sv['t'] == "LineBreak":
                  curstr = curstr + ' '
              else: #othe items , just keep them
                  if len(curstr) > 0 :
                      out.append(Str(transWrapper(curstr,"Para")))
                      curstr=""
                  out.append(sv)
              #print "out put:", out
          if len(curstr) > 0:
              out.append(Str(transWrapper(curstr)))
          #print 'final out for the para:' , out
          if key == 'Para' :
              return Para(out)
          elif key == 'Plain':
              return Plain(out)
      #assume simple strong ,Emph and header, no more sub structure in the strong/Emph/Header
      elif key == 'Strong':
          #print "Strong"
          if debug == 1:
              fh.write("Strong \n")
          hstr = stringify(value)
          trStr=transWrapper(hstr)
          return Strong([Str(trStr)])
      elif key == 'Emph':
          #print "Emph"
          if debug == 1:
              fh.write("Emph\n")
          hstr = stringify(value)
          trStr=transWrapper(hstr)
          return Emph([Str(trStr)])
      elif key == 'Header':
          #print "Header"
          if debug == 1:
              fh.write("Header\n")
          hstr = stringify(value[2])
          trStr=transWrapper(hstr,"Header")
          return Header(value[0],value[1],[Str(trStr)])
      elif key == 'Link':
          #print "Link"
          if debug == 1:
              fh.write("Link\n")
          hstr = stringify(value)
          trStr=""
          if len(hstr) < 1:
            trStr=""
            return []
          else:
            trStr=transWrapper(hstr,"Link")
          return Link(value[0],[Str(trStr)],value[2])
      else:
          return None

if __name__ == "__main__":
  toJSONFilter(transPara)
