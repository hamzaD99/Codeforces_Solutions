word = input()
letters = []
count = 0
for l in word:
	if l not in letters:
		count+=1
		letters.append(l)
if count%2 == 0:
	print("CHAT WITH HER!")
else:
	print("IGNORE HIM!")