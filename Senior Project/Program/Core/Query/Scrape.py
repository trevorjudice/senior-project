import sys

import urllib2
import StringIO
import gzip

from apiclient.http import BatchHttpRequest
from googleapiclient.discovery import build

class Scraper:
  def __init__(self):
    self.snippets = []
    self.snippets_string = []
    self.links = []
  def build_array(self,request_id, response, exception):
    snippet = ""
    if response is not None:
      if 'items' in response:
          for item in response[u'items']:
            snippet += ''.join(s for s in item[u'snippet'] if ord(s)>31 and ord(s)<126)
          for item in response[u'items']:
            if "wikipedia" in item[u'link'].lower():
              self.links.append(item[u'link'].encode('utf-8'))
      self.snippets_string.append(snippet.encode('utf-8'))
    else:
      print exception
  def q_arr(self,request_id, response, exception):
    snippet = ""
    if response is not None:
      if 'items' in response:
          for item in response[u'items']:
            snippet += ''.join(s for s in item[u'snippet'] if ord(s)>31 and ord(s)<126)
          if "wikipedia" in item[u'link'].lower():
              self.links.append(item[u'link'].encode('utf-8'))
      self.snippets.append([snippet.encode('utf-8')])
    else:
      print exception
  def Scrape(self,args):
    self.service = build("customsearch", "v1", developerKey="AIzaSyCB2POu33UfqBrNpYQVbV5VVCHH6HPQWCI")
    self.batch = self.service.new_batch_http_request()
    for query in args:
      res = self.service.cse().list(
          q=query,
          cx='003626414652166372216:p7uc0qsmrgg',
          fields="items(snippet),items(link)"
      )
      if query == args[0]:
        self.batch.add(res,callback=self.q_arr)
      else:
        self.batch.add(res,callback=self.build_array)
    self.batch.execute()
    self.snippets.append(self.snippets_string)
    return [self.snippets,self.links]