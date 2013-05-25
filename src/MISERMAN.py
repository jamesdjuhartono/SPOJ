n, m = map(int,raw_input().strip().split())
matrix = [map(int,raw_input().strip().split()) for x in xrange(n)]
#print matrix
for i in xrange(1,n):
	for j in xrange(m):
		way1 = 100000000
		way2 = 100000000
		way3 = 100000000

		if j-1 >= 0:
			way1 = matrix[i-1][j-1]

		way2 = matrix[i-1][j]

		if j+1 < m:
			way3 = matrix[i-1][j+1]

		matrix[i][j] += min(way1, way2, way3)

if n == 0:
	print 0
else:
	print min(matrix[n-1])