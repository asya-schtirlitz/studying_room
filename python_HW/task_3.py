


def countPairsInList(list):
	dict = {}
	dict = dict.fromkeys(list)
	s = 0
	for key in dict.keys():
		s = s + counter(list.count(key))
	return s
		
def counter(number):
	s = 0
	for i in range(number):
		s = s+i
	return s
	
if __name__ == '__main__':
	print(countPairsInList([1,2,3,1,2,3,5]))
	print(countPairsInList([1,1,1,1,5]))
	print(countPairsInList([1,5]))
	print(countPairsInList([]))