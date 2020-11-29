import sys
In = input()
count = 1
lastOne = In[0]
for l in In:
	if l == lastOne:
		count += 1
	else:
		count = 1
		lastOne = l
	if count == 7:
		print("YES")
		sys.exit()
print("NO")