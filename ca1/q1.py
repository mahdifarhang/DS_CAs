from __future__ import division
from operator import itemgetter
G, N = map(int, raw_input().split())
nutrient = [int(x) for x in raw_input().split()]
weight = [int(x) for x in raw_input().split()]
c = list(reversed(sorted([[x, y, x/y] for x, y in zip(nutrient, weight)], key=itemgetter(2))))
sumofweight = sumofnutrient = i = 0
for i in xrange(len(c)):
	if (c[i][1] + sumofweight < G):
		sumofweight += c[i][1]
		sumofnutrient += c[i][0]
	else:
		sumofnutrient += (G - sumofweight) / c[i][1] * c[i][0]
		break
print(sumofnutrient)