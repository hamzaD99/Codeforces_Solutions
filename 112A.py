word1 = input()
word2 = input()

word1 = word1.lower()
word2 = word2.lower()
def count(x, y):
	if x < y:
		return -1
	elif x > y:
		return 1
	else:
		return 0
def res():
	for l in range(len(word1)):
		res = count(word1[l], word2[l])
		if res == 0:
			continue
		return res
	return 0
print(res())