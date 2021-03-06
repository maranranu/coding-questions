"""
You are given an array A of size n. In one move, you can select a subarray of size 3. 
Let those indices be i - 1, i and i + 1. We add A[i] to our total score and then change A[i], A[i - 1] and A[i + 1] to 0. 
We repeat this process untill the entire array becomes 0. 
If we select the subarrays optimally, what is the maximum score that can be achieved?.
Input format:

First line contains one integer t, denoting the number of test cases.

Each testcase is provided as follows:-

First line contains one integer n, denoting the size of array.

Next line contains n integers (a1, a2, ... an), representing the array.

Output format:

For each test case, print the maximum achievable score in a new line.
"""
def max_score(arr, score=0):
    maxElem = arr[1]
    maxIndex = 1
    
    for i in range(2, len(arr)-1):
        temp = arr[i]
        if temp >= maxElem:
            maxElem = temp
            maxIndex = i
    if maxElem == 0:
        return score

    if maxIndex > 0 and maxIndex < len(arr)-1:
        score += arr[maxIndex]
        arr[maxIndex-1] = 0
        arr[maxIndex+1] = 0
        arr[maxIndex] = 0
        
    return max_score(arr, score)


def max_score_dp(arr):
    dp = []
    dp.append(0)
    dp.append(arr[1])

    for i in range(2, len(arr)-1):
        temp = max(dp[i-1], dp[i-2] + arr[i])
        dp.append(temp)
        n = i

    return dp[-1]

t = int(input())

for i in range(t):
    n = int(input())
    arr = (input()).split(" ")
    arr = [int(a) for a in arr]
    result = max_score_dp(arr)
    print(result)

"""
st = "65 74 5 48 53 5 9 63 97 79 49 16 94 26 29 10 28 60 64 76 61 38 65 21 22 21 2 21 81 65 30 49 51 7 15 54 43 39 31 21 1 87 80 26 60 92 28 59 9 35 70 80 20 47 11 29 26 57 65 3 82 21 62 5 26 85 38 32 89 52 58 11 50 9 37 13 100 18 5 67 65 84 79 53 98 68 65 61 77 9 61 93 2 13 50 91 8 83 14 22"
st = "44 13 78 20 45 63 13 41 94 39 69 8 86 96 96 42 66 14 52 76 69 100 76 16 33 35 60 28 47 70 59 63 24 66 11 25 72 48 16 62 11 1 18 46 71 25 17 12 77 97 3 53 17 8 73 61 97 18 44 9 31 61 63 79 34 64 69 99 98 13 48 95 28 2 9 31 86 79 76 51 13 88 29 42 84 83 49 83 60 66 79 55 9 15 30 15 32 4 59 19"
st = "70 21 97 27 18 78 81 29 21 100 11 68 90 22 21 19 91 29 36 11 84 11 96 45 14 26 64 74 58 9 14 45 9 80 99 27 79 78 9 61 49 43 86 25 32 88 66 78 96 85 38 96 62 49 71 57 49 85 71 15 52 67 26 34 33 61 21 69 87 11 4 97 35 10 49 87 5 19 7 31 41 12 93 41 12 86 72 4 72 29 87 6 21 21 81 12 8 73 26 50"
arr = st.split(" ")
arr = [int(a) for a in arr]

result = max_score_dp(arr)
print(result)
"""
