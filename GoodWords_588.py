#GoodWords_588

word = input()

def isVowel(x):
	if x =='a' or x =='e' or x =='i' or x =='o' or x =='u':
		return True
	else:
		return False

def goodWord(word):
	for i in range(0, len(word)-1):
		if isVowel(word[i]) or isVowel(word[i+1]):
			pass
		else:
			return "NO"

	return "YES"

print(goodWord(word))
