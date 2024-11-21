def mn(x):
    a = []
    for i in range(10):
        a.append(min(x))
        x.remove(min(x))
    return a

def mx(x):
    a = []
    for i in range(10):
        a.append(max(x))
        x.remove(max(x))
    return a

f = [int(x) for x in open('17.2.txt')]
cnt = 0
mxs = 0
mas = [*(mn(f)),*(sorted(mx(f)))]
for i in range(len(mas)-2):
    if (mas[i]+mas[i+2] > sum(mas)/len(mas)):
        cnt += 1
        if (mas[i] + mas[i+2] > mxs):
            mxs = mas[i] + mas[i+2]
print(cnt)
print(mxs)