import itertools

multime=set({"A","B","C","D"})
for i in range(1,len(multime)+1):
    subsets=set((itertools.combinations(multime, i)))
    print(subsets)
