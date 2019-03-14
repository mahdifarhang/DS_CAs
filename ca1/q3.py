from __future__ import division
n, w = map(int, raw_input().split())
line = list(reversed(sorted([int(x) for x in raw_input().split()])))
for i in xrange(n):
	line += ([line[0]/2]*2)
	del line[0]
line = sorted(line)
final = 3 * n * line[0]
if (final > w):
	print(w)
else:
	print(final)