

def cropWord(word):
	i = len(word)
	while i > 0:
		print(word[:i])
		i -= 1
		
def loopWord(word):
	i = len(word)
	while i>0 :
		print(word[i:]+word[:i])
		i -=1
		
if __name__ == '__main__':
	cropWord("abracadabra")
	print();
	loopWord("abracadabra")