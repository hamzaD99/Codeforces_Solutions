n = input()
word = input()
colors = []
last = 0
count = 0
for x in range(int(n)):
	colors.append(word[x])
for c in colors:
	if c == last:
		count += 1
	else:
		last = c
print (count)