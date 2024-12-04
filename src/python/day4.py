
def ptI(f):
    arr = []
    ans = 0
    for line in f.readlines():
        arr.append([i for i in line if i != "\n"])

    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            ans += find_sol(arr, i, j)
    return ans

def find_sol(arr, x, y):
    word = 'XMAS'
    n = len(arr) # rows
    m = len(arr[0]) # cols
    ans = 0
    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1), # Left
        (-1, 0), # Up
        (1, 1),  # Diagonal Down-Right
        (-1, -1),# Diagonal Up-Left
        (1, -1), # Diagonal Down-Left
        (-1, 1)  # Diagonal Up-Right
    ]
    for dx, dy in directions:
        xb = x+ 3*dx 
        yb = y+3*dy
        if xb >= 0 and xb < m and yb >= 0 and yb < n:
            s = ""
            for i in range(4):
                s+= arr[x+dx*i][y+dy*i]
            if s == word:
                ans += 1
    return ans

def ptII(f):
    arr = []
    ans = 0
    for line in f.readlines():
        arr.append([i for i in line if i != "\n"])

    for i in range(len(arr)):
        row = arr[i]
        for j in range(len(row)):
            ans+=check_sol(arr,i,j)
    return ans

def check_sol(arr, x,y):
    n = len(arr) # rows
    m = len(arr[0]) # cols
    xb = x+2
    yb = y+2
    cnt = 0
    if xb < m and yb < n:
        #MS
        #MS
        if arr[x][y] == 'M' and arr[x+2][y]=='S' and arr[x+1][y+1]=='A' and arr[x][y+2] == 'M' and arr[x+2][y+2]=='S':
            cnt+= 1
        #SM
        #SM
        elif arr[x][y] == 'S' and arr[x+2][y]=='M' and arr[x+1][y+1]=='A' and arr[x][y+2] == 'S' and arr[x+2][y+2]=='M':
            cnt+= 1
        #SS
        #MM
        if arr[x][y] == 'S' and arr[x+2][y]=='S' and arr[x+1][y+1]=='A' and arr[x][y+2] == 'M' and arr[x+2][y+2]=='M':
            cnt+= 1
        #MM
        #SS
        elif arr[x][y] == 'M' and arr[x+2][y]=='M' and arr[x+1][y+1]=='A' and arr[x][y+2] == 'S' and arr[x+2][y+2]=='S':
            cnt+= 1
         
    return cnt
