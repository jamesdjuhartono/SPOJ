while True:
	sentence = map(str, raw_input().lower().split())
	if sentence[0] == '*':
		break
	tautogram = False
	wordset = set([words[0] for words in sentence])
	if len(wordset) > 1:
		print "N"
	else:
		print "Y"