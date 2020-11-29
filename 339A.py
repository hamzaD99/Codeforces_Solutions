prob = input().split("+")
prob.sort()
text = ""
for x in prob:
	text += x + "+"
print(text[:-1])