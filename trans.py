#!/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import random
import json
import time

appid = 'youridhere'
secretKey = 'yourkey'

def trans(qq): 
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = qq
    fromLang = 'en'
    toLang = 'zh'
    salt = random.randint(32768, 65536)
    
    sign = appid+q+str(salt)+secretKey
    m1 = md5.new()
    m1.update(sign)
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
     
    try:
        httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
     
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        dd=json.loads(response.read())
        return dd["trans_result"]
        #for ii in dd["trans_result"]:
        #  print ii['src']
        #  print ii['dst']
    except Exception, e:
        a = 1
        #fe=open('terror.dat',"w")
        #fe.write(e)
        #fe.close()
        #print e
    finally:
        if httpClient:
            httpClient.close()

def transWrapper(content):
    return '@@%s@@'%content
    time.sleep(0.1)
    res = trans(content)
    out=""
    if res != None:
      for ii in res:
          out = out + ii['dst']
    return out


from pandocfilters import toJSONFilter, Emph, Para, Str, stringify, Header , Strong, Plain

def transPara(key, value, format, meta):
      if key == 'Para'  or key == 'Plain':
          out= []
          curstr=""
          for sv in value:
              #print "processing...", sv
              if sv['t'] == "Str":
                  curstr = curstr + sv['c'] 
              elif sv['t'] == "Space" or sv['t'] == "SoftBreak" or sv['t'] == "LineBreak":
                  curstr = curstr + ' '
              else: #othe items , just keep them
                  if len(curstr) > 0 :
                      out.append(Str(transWrapper(curstr)))
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
          hstr = stringify(value)
          trStr=transWrapper(hstr)
          return Strong([Str(trStr)])
      elif key == 'Emph':
          hstr = stringify(value)
          trStr=transWrapper(hstr)
          return Emph([Str(trStr)])
      elif key == 'Header':
          hstr = stringify(value)
          trStr=transWrapper(hstr)
          return Header(value[0],value[1],[Str(trStr)])
      else:
          return None

if __name__ == "__main__":
  toJSONFilter(transPara)
