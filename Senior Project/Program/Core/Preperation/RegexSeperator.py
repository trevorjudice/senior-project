#!/usr/bin/env python	

"""Returns list of question and answer choices from unformatted text"""

__author__      = "Trevor Judice"

def RegexSeperator(text):

	choices = []

	split_text = text.split('?')
	split_text[0] = split_text[0].replace('\n',' ')

	question = ''.join(s for s in split_text[0] if ord(s)>31 and ord(s)<126)
	print "Beggining to search for answer to Question: "+question
	answers = split_text[1].split('\n\n')

	for answer in answers:
		if len(answer)>1:
			ans = ''.join(s for s in answer if ord(s)>31 and ord(s)<126)
			choices.append(ans)
	print "With answers: "+str(choices)
	
	return [question,choices]

if __name__ == "__main__":
	
	RegexSeperator(sys.argv[0])