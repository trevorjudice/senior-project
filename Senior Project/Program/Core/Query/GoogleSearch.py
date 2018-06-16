import sys

import urllib2
import StringIO
import gzip

from apiclient.http import BatchHttpRequest
from googleapiclient.discovery import build


my_api_key = "AIzaSyCB2POu33UfqBrNpYQVbV5VVCHH6HPQWCI"
my_cse_id = "003626414652166372216:p7uc0qsmrgg"

def GoogleSearch(search_terms, **kwargs):
	results = []
	links = []
	snippets = []
	service = build("customsearch", "v1", developerKey="AIzaSyCB2POu33UfqBrNpYQVbV5VVCHH6HPQWCI")
	if search_terms == str(search_terms):
		res = service.cse().list(q=search_terms, cx="003626414652166372216:p7uc0qsmrgg", **kwargs).execute()
		results.append(res["items"])
	else:
		for search_term in search_terms:
			res = service.cse().list(q=search_term, cx="003626414652166372216:p7uc0qsmrgg", **kwargs).execute()
			results.append(res["items"])
	for result in results:
		for resu in result:
			links.append(resu["link"])
			snippets.append(resu["snippet"])
	return [links, snippets]

if __name__ == "__main__":
	GoogleSearch(sys.argv[0],num=10)

