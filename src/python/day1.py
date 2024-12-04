import math

def ptI():
    file = open("day1.txt", 'r')
    l1 = []
    l2 = []
    for lines in file.readlines():
        #print(lines.strip())
        temp = lines.strip().split()
        l1.append(int(temp[0]))
        l2.append(int(temp[1]))
    l1.sort()
    l2.sort()
    ans = 0
    for i in range(len(l1)):
        ans += abs(l1[i]-l2[i])
    return ans

def ptII():
    file = open("day1.txt", 'r')
    l1 = []
    d2 = {}
    for lines in file.readlines():
        #print(lines.strip())
        temp = lines.strip().split()
        l1.append(int(temp[0]))

        t = int(temp[1])
        if t in d2:
            d2[t]+=1
        else:
            d2[t] = 1

    ans = 0
    for i in l1:
        if i in d2:
            ans += i*d2[i]
    return ans

if __name__ == "__main__":
    print(ptII())
