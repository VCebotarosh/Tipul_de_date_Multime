import itertools

multime=set({1,2,3,4})
for i in range(1,len(multime)+1):
    subsets=set(itertools.combinations(multime, i))
    print(subsets)
