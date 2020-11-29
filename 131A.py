Word = input()
if Word.isupper():
	print(Word.lower())
else:
	if len(Word) > 1:
		WordL = Word[1:]
		if WordL.isupper() and Word[0].islower():
			print(Word[0].upper()+WordL.lower())
		else:
			print(Word)
	else:
		print(Word.upper())