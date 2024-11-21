def mn(x):
    a = []
    for i in range(5):
        a.append(min(x))
        for i in range(x.count(min(x))):
            x.remove(min(x))
    return a[-1]

def mx(x):
    a = []
    for i in range(3):
        a.append(max(x))
        for i in range(x.count(max(x))):
            x.remove(max(x))
    return a[-1]

f = [int(x) for x in open('17.3.txt')]
cnt = 0
mas = []
mxs = 0
e = mn(f) + mx(f)
for i in range(len(f)-2):
    if (f[i]*f[i+1]*f[i+2] >= (e) * 2):
        mas.append(f[i])
        mas.append(f[i]+1)
        mas.append(f[i]+2)
mas = sorted(mas)
for i in range(len(mas)-4):
    if ((mas[i] < 90 and mas[i+2] < 90 and mas[i+4] < 90) and (mas[i] + mas[i+2] + mas[i+4] == 180)):
        cnt += 1
        if (mas[i] * mas[i+2] * mas[i+4] > mxs):
            mxs = mas[i] * mas[i+2] * mas[i+4]
print(mas)
print(cnt)
print(mxs)