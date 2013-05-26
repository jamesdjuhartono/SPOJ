#formula reference: http://www.maths.surrey.ac.uk/m_maths/ug/downloads/blackboard_1.pdf
tc = int(raw_input())
for i in xrange(tc):
	n = int(raw_input())
	if n % 2 == 0:
		print (n*(n+2)*(2*n+1))/8
	else:
		print ((n+1)*(2*n**2 + 3*n -1))/8