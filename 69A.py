n = int(input())
vectors = []
vect_f = []
sum = [0, 0, 0]
for line in range(n):
	vectors.append(input())
for x in vectors:
	temp = []
	te = []
	temp = x.split()
	for y in temp:
		te.append(int(y))
	vect_f.append(te)
for r in range(n):
	sum[0] += vect_f[r][0]
	sum[1] += vect_f[r][1]
	sum[2] += vect_f[r][2]
if sum[0] == 0 and sum[1] == 0 and sum[2] == 0:
	print("YES")
else:
	print("NO")