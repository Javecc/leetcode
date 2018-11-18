#if a+b+c=1000,and a^2+b^2=c^2,put out a,b,c
import time

start_time = time.time()
for a in range(0,1001):
	for b in range(0,1001):
			c = 1000 - a - b
			if a**2 + b**2 == c**2:
				print("a = {},b = {},c = {}".format(a,b,c))
end_time = time.time()
print("time = {}".format(end_time-start_time))