tests = int(input())
for i in xrange(tests):
	a, b = map(int, raw_input().split())
	line = [int(x) for x in raw_input().split()]
	time = 0
	while True:
		if(line[0]<max(line)):
			line.append(line[0])
			del line[0]
		else:
			del line[0]
			time += 1
			if (b==0):
				break
		b += -1
		if (b== -1):
			b=len(line)-1
	print(time)
