#!/usr/bin/env python

"""Returns Google Cloud Entities, referenced by entities.name, entities.salience, entity_type[entity.type]"""

__author__	  = "Trevor Judice"

import RAKE

r = RAKE.rake()

text = "Who was the first president of the united states?"

print r.extract_keywords_from_text(text)