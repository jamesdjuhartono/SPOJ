def common(s1, s2):
	store = []
	for char in s1:
		try:
			s2.remove(char)
			store.append(char)
		except:
			pass
	store.sort()
	return store

while True:
	try:
		s1 = list(raw_input())
		s2 = list(raw_input())
		print "".join(common(s1, s2))
	except:
		break