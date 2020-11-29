word = input()
Vowels = ["a","o","y","e","u","i"]
word = word.lower()
Fword = ""
for l in word:
	if l not in Vowels:
		Fword += "."
		Fword += l
print(Fword)