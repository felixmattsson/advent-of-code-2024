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
    print(ans)
