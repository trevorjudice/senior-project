#!/usr/bin/env python

"""Returns Google Cloud Entities, referenced by entities.name, entities.salience, entity_type[entity.type]"""

__author__	  = "Trevor Judice"

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/trevorjudice/Downloads/Trivia-61cc592363c1.json"

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

important_words = ["first","second","last","only","third"]
def SalientTerms(question):

	cloud = language.LanguageServiceClient()
	
	document = types.Document(
		content=question,
		type=enums.Document.Type.PLAIN_TEXT)

	entities = cloud.analyze_entities(document).entities

	entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION','EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

	ret = [entity for entity in entities]

	ret = " ".join(entity.name for entity in ret)

	imp = ""
	for word in important_words:
		if word.lower() in question.lower() and not word.lower() in ret.lower():
			imp +=" "+word
	return imp + " "+ret

if __name__ == "__main__":
	SalientTerms(sys.argv[0])