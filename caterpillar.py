def caterpillar(A,s):
    n = len(A)
    front = total = 0

    for back in range(n):
        while(front<n and total+A[front]<s):
            total += A[front]
            front += 1
        if(total==s):
            return 1

        total -= A[back]

    return 0

a = [6,2,7,4,1,3,6]
print(caterpillar(a,12))