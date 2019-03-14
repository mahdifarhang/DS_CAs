a, b, k=map(int, raw_input().split())
stack = []
for i in xrange(a):
	stack.insert(0, raw_input())
for i in xrange(b):
	temp = raw_input()
	if(temp[0]=='A'):
		stack.append(temp[4:-1])
	else:
		if(k > len(stack)):
			stack.append(stack[0])
			del stack[0]
		else:
			stack.append(stack[-1 * k])
			del stack[((-1) * k) - 1]
for i in xrange(len(stack)):
	print(stack[len(stack) - i -1])