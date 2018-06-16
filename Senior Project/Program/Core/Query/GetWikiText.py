#!/usr/bin/env python

"""Returns text of given list of wikipedia links"""

__author__	  = "Trevor Judice"

from googleapiclient.discovery import build

import json

import requests

from bs4 import BeautifulSoup

import sys

def GetWikiText(links):
	final = []
	for link in links:
		a = requests.get(link)
		soup = BeautifulSoup(a.text, 'html.parser')
		results = soup.find_all('p')
		res = [item.get_text().encode('utf-8') for item in results]
		final.append(res)
	return final
if __name__ == "__main__":
	GetWikiText(sys.argv[0])