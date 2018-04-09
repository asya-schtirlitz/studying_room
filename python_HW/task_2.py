

def changeList(l1):
	k = 0
	l2=[]
	while k<=len(l1):
		if k+1<len(l1):
			l2.append(l1[k+1])
		l2.append(l1[k])
		k += 2
	l1.clear()
	l1.extend(l2)
	
if __name__ == '__main__':
	list = [0,1,2,3,4,5,6]
	changeList(list)
	print("after changing ",list)