import re
def ptI(f):
    #print('hi')
    txt = f.read()
    ans = 0
    matches = re.findall(r"mul\(\d+,\d+\)|don't\(\)|do\(\)", txt)
    do = True
    for s in matches:
        if s == "don't()":
            do = False
        elif s == "do()":
            do = True
        elif do: 
            num1, num2 = re.findall(r'\d+', s)
            ans += int(num1) * int(num2)

    return ans

def ptII(f):
    pass