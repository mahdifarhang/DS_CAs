n, q = map(int, raw_input().split())
groups = sorted([int(x) for x in raw_input().split()])
Destroyed = [0] * (n + 1)
result = [0] * n
for i in xrange(q):
	low, high = map(int, raw_input().split())
	Destroyed[low-1]+=1
	Destroyed[high]-=1
temp = 0
for i in xrange(n):
	temp+=Destroyed[i]
	result[i] = temp
result = sorted(result)
print(sum(a*b for a,b in zip(result, groups)))