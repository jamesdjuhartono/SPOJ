def initMatrix():
	mat = []
	for i in xrange(105): #rows
		mat.append([])
	for j in xrange(105): #cols
		mat[0].append(0)
		if j == 0:
			mat[1].append(2)
			mat[2].append(3)
		elif j == 1:
			mat[1].append(0)
			mat[2].append(1)
		else:
			mat[1].append(0)
			mat[2].append(0)

	for i in xrange(3,105):
		for j in xrange(105):
			if j == 0:
				mat[i].append(mat[i-1][j] + mat[i-2][j])
			else:
				mat[i].append(mat[i-1][j] + mat[i-1][j-1] + mat[i-2][j] - mat[i-2][j-1])

	return mat

matrix = initMatrix()

tc = int(raw_input())
for i in xrange(tc):
	num, n, k = raw_input().split(' ')
	print str(num) + " " + str(matrix[int(n)][int(k)])