mat = []
matF = []
for x in range(5):
	mat.append(input())
for x in mat:
	temp = []
	for y in x:
		if y != " ":
			temp.append(int(y))
	matF.append(temp)
def printM(Mat):
	print("-------------------------")
	for n in Mat:
		for nn in n:
			print(str(nn), end=" ")
		print()
def swapR(Mat, r, e):
	new_mat = []
	new_mat = Mat
	temp = new_mat[r-1]
	new_mat[r-1] = Mat[e-1]
	new_mat[e-1] = temp
	return new_mat
def swapC(Mat, r, e):
	new_mat = []
	new_mat = Mat
	r_col = []
	e_col = []
	for row in new_mat:
		r_col.append(row[r-1])
		e_col.append(row[e-1])
	for x in range(5):
		new_mat[x][r-1] = e_col[x]
		new_mat[x][e-1] = r_col[x]

r = -1
e = -1
for row in range(5):
	for col in range(5):
		if matF[row][col] == 1:
			r = row
			e = col
			break
	if r and e != -1:
		break
F_RES = abs(r-2)+abs(e-2)
print(F_RES)