import matplotlib.pyplot as plt
import numpy as np

def flipped(n):
    num=str(n)
    l=list(num)
    l.reverse()
    return int(''.join(l))

def checkPalindrome(n):
    if n==flipped(n):
        return True
    else:
        return False

l1=[]
x=[]
y=[]

def solve(number):
    count=0
    n=number
    while True:
        if checkPalindrome(number)==True:
            # print(f'palindrome: {number}')
            break
            # return number
        # print(f'{number} + {flipped(number)}')
        number=number+flipped(number)
        count+=1
        if count>=1000:
            count=-1
            t='threshold crossed'
            global l1
            y.append(n)
            break
    # return count
    # print (f'{n} : {count}')
    # print (f'steps for {n}: {count}')
    # print('-------------------')


for i in range(0,10000):
    solve(i)

for i in range(len(y)):
    x.append(i)

# print(x)
# print('---')
# print(y)

xpoints = np.array(x)
ypoints = np.array(y)
# plt.scatter(xpoints,ypoints, s=0.01,c='black')
plt.plot(ypoints)
plt.show()

