#!/usr/bin/env python

"""Generates Queries for tests"""

__author__      = "Trevor Judice"


def GenerateQueries(question,answers):
	
	ret = []
	
	for i in range(0,len(answers)):
		
		ret.append(question+" "+answers[i])

	return ret


if __name__ == "__main__":
	
	GenerateQueries(sys.argv[0],sys.argv[1])