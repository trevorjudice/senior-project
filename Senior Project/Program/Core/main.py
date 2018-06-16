#!/usr/bin/env python
	
"""Runs the Trivia Program"""

__author__	  = "Trevor Judice"

import Preperation
import Query
from rake_nltk import Rake
import time

import csv
import cv2
from PIL import Image

import pytesseract

import numpy as np
np.set_printoptions(threshold=np.nan)

sum_capped = []



question = "What word describes joining a cause just to feel good about it"
answers =  ["Joinerism","Gung-faux", "Slacktivism"]

# while True:
# 	question = ''
# 	raw_choices = []
# 	results = []
# 	capped = Preperation.GrabScreen()
# 	capped_gray = cv2.cvtColor(np.array(capped),cv2.COLOR_BGR2GRAY)
# 	if np.sum(capped_gray)>100000000:
# 		time.sleep(.5)
# 		capped = Preperation.GrabScreen()
# 		capped_gray = cv2.cvtColor(np.array(capped),cv2.COLOR_BGR2GRAY)
		
# 		text = pytesseract.image_to_string(Image.fromarray(capped_gray))

# 		if len(text)>1:
			
# 			seperate = Preperation.RegexSeperator(text)
# 			choices = seperate[1]
			
# 			for ans in choices:
# 				raw_choices.append(ans)
# 			question = seperate[0]
# 			print GeneralSearch(Preperation.GenerateQueries(question,raw_choices),raw_choices)


def GeneralSearch(queries,answers):

	#answers = ["Obama","Trump","Bush"]

	scores = [0,0,0]
	wikiLinks = []
	results = Query.GoogleSearch(queries)
	
	links = results[0]
	snippets = results[1]
	
	for link in links:
		
		if "wikipedia" in link:
				
			wikiLinks.append(link)

	wikiText = Query.GetWikiText(wikiLinks)

	for article in wikiText:
		article = " ".join(ele for ele in article)
		article = article.split(" ")
		for word in article:
			
			for i in range(0,len(scores)):
				for ans in answers[i].split(" "):
					if ans.lower() in word.lower():
						scores[i] += 1
	for snippet in snippets:

		snippet = snippet.split(" ")
		
		for word in snippet:
			
			for i in range(0,len(scores)):
				for ans in answers[i].split(" "):
					if ans.lower() in word.lower() and len(ans)>3:
						scores[i]+=1
	return scores
def SalientTermsTest(answers, terms):
	
	scores = [0,0,0]
	
	term_list = terms.lower().split(" ")

	for i in range(0,3):

		wikiLinks = []
		results = Query.GoogleSearch(answers[i])
		links = results[0]
		snippets = results[1]
	
		for link in links:
		
			if "wikipedia" in link:
				
				wikiLinks.append(link)
		wikiText = Query.GetWikiText(wikiLinks)
		s = ""
		for article in wikiText:
			for a in article:
				s+=a
		s = Preperation.SalientTerms(s)
		article = ''.join(a for a in s if ord(a)>31 and ord(a)<126)
		article = article.split(" ")
		for word in article:
			for term in term_list:
				if term in word.lower() and len(term) > 3:
					scores[i]+=1
	return scores
final_scores = [0,0,0]
qs = 0
cor = 0
def addScores(ansScores):
	for i in range(0,len(ansScores)):
		final_scores[i]+=ansScores[i]


csv_in = open('hqQuestions.csv', 'rb')
reader = csv.reader(csv_in)

for row in reader:
	question,a1,a2,a3,ans = row

	print question
	final_scores = [0,0,0]
	answers = [a1,a2,a3]

	# addScores(GeneralSearch([Preperation.SalientTerms(question)],answers))
	#addScores(SalientTermsTest(answers, Preperation.SalientTerms(question)))
	addScores(GeneralSearch(Preperation.GenerateQueries(question,answers),answers))
	addScores(GeneralSearch([question],answers))

	max_ind = 0
	for i in range(0,len(answers)):
		if final_scores[i] > final_scores[max_ind]:
			max_ind = i
	print "Answer Given: " + answers[max_ind]
	print "Correct Answer: "+ans
	print "Scores:"
	print answers[0]+": "+str(final_scores[0])
	print answers[1]+": "+str(final_scores[1])
	print answers[2]+": "+str(final_scores[2])
	if answers[max_ind] == ans:
		cor+=1
	qs+=1
	print "Questions right: "+str(cor)+" out of "+str(qs)+" total"




print final_scores