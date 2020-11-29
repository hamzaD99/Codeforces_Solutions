n = input()
words = []
output = []
for word in range(int(n)):
	w = input()
	words.append(w)
for Word in words:
	if len(Word) <= 10:
		output.append(Word)
	else:
		x = Word[0]+str(len(Word)-2)+Word[-1]
		output.append(x)
for o in output:
	print(o)