from math import factorial

f = [int(x) for x in open('17.1.txt')]
cnt = 0
mx = 0
mas = []
mxs = max(f)
mns = min(f)
for i in range(len(f)-1):
    if (factorial(f[i]) * factorial(f[i+1]) > factorial(mxs) - factorial(mns)):
        mas.append(f[i])
        mas.append(f[i+1])
for i in range(len(mas)//2):
    if (mas[i] % 2 == 0 or mas[(i+1)*-1] % 2 == 0):
        cnt += 1
        if mx < mas[i] + mas[(i+1)*-1]:
            mx = mas[i] + mas[(i+1)*-1]
print(mas,cnt,mx)
