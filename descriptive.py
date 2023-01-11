nlist = [2, 4, 7, 3, 1, 13]
nlisteven = nlist + [9]
rlist = [3.14, 2.58, -6.78, -3,74]
rlisteven = rlist + [90.3]

import statistics
statistics.mean(nlist)
statistics.mean(rlist)

print(nlist)
print(sorted(nlist))

statistics.median(nlist)

print(nlisteven)
print(sorted(nlisteven))

statistics.median(nlisteven)

print(rlist)
print(sorted(rlist))

statistics.median(rlist)

print(rlisteven)
print(sorted(rlisteven))

statistics.median(rlisteven)

mlist = [2, 3, 4, 5, 3, 6, 1, 3]
print(mlist)
print(sorted(mlist))
statistics.mode(mlist)
statistics.stdev(rlist)
statistics.variance(rlist)

