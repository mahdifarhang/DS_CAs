line = int(input())
last = []
for i in xrange(line):
	a = [int(x) for x in raw_input().split()]
	if(a[0]==1):
		last.append(a[1])
	elif (a[0]==2):
		del last[-1]
	elif(a[0]==3):
		if(len(last)==0):
			print("Empty!")
		else:
			print(last[-1])