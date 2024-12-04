

def ptI():
    file = open("day2.txt", 'r') 
    ans = 0
    for lines in file.readlines():
        words = lines.strip().split()
        pos = 1
        if int(words[0]) > int(words[1]):
            pos = -1

        valid = True
        for i in range(len(words)-1):
            l = int(words[i])
            r = int(words[i+1])
            if pos*(r-l) < 1 or pos*(r-l) > 3:
                valid = False
        if valid:
            ans+=1

    return ans

def ptII(f):
    #clean solution taken from another repo as my previous solution was not as clean
    lines = [[int(x) for x in line.split()] for line in f.read().splitlines()]
    ans = 0
    for real_nums in lines:
        for i in range(len(real_nums) + 1):
            nums = real_nums[:i] + real_nums[i + 1 :]
            if nums not in (sorted(nums), sorted(nums, reverse=True)):
                continue
            if not all(1 <= abs(b - a) <= 3 for a, b in zip(nums, nums[1:])):
                continue
            break
        else:
            continue
        ans += 1
    return ans

if __name__ == "__main__":
    file = open("day2.txt", 'r') 
    print(ptII(file))
