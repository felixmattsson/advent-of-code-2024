with open('input.txt') as f:
    a = []
    b = []
    for line in f:
        # print(line[8:13])
        a.append(int(line[0:5]))
        b.append(int(line[8:13]))
    a.sort()
    b.sort()

    import numpy as np
    a = np.array(a)
    b = np.array(b)
    c = abs(a-b)
    ans = sum(c)
    print("ans to first: ", ans)

# Second part
# print(a.value_counts())
import collections
unique, counts = np.unique(a, return_counts=True)
a_dict = dict(zip(unique, counts))
print(a_dict)
unique, counts = np.unique(b, return_counts=True)
b_dict = dict(zip(unique, counts))
# print(b_dict)
d = []
for element in a:
    print(element)
    d.append(element*np.count_nonzero(b==element))
d=np.array(d)
ans_2 = np.sum(d)
print(ans_2)