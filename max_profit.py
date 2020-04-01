A = [0] * 6
A[0] = 23171
A[1] = 21011
A[2] = 21123
A[3] = 21366
A[4] = 21013
A[5] = 21367

def prof(A):
    maxSlice = maxi = A[0]
    for a in A[1:]:
        maxSlice = max(maxSlice, maxSlice+a)
        maxi = max(maxi, maxSlice)

    print(maxi)



def solution(A):
    # write your code in Python 3.6
    #tab des diff
    if len(A) < 2:
        return 0

    diff = [0]*len(A)
    for i in range(1, len(A)):
        diff[i] = (A[i]-A[i-1])

    maxSlice = maxi = 0

    for e in diff[1:]:

        maxSlice = max(e, maxSlice + e)

        maxi = max(maxi, maxSlice)

    return maxi

# b = [8, 9, 3, 6, 1, 2]
