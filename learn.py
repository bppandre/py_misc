def triangle(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end=' ')
        print('')

# triangle(4)

def reverse_triangle(n):
    for i in range(n-1, 0, -1):
        for t in range(n-i-1):
            print(' ',end=' ')
        for j in range(2*i-1):
            print('*',end=' ')
        print('')

# reverse_triangle(6)

def counting_digits(n):
    num = n
    res = 0
    while n>0:
        res+=1
        n//=10
    print()
    print(num, 'has:', res,'digits')

# counting_digits(1)
# counting_digits(22)
# counting_digits(345)

### testing neg range

# for i in range(15,2,-1):
#     print(i)
# for i in range(15,2,-2):
#     print(i)
# for i in range(15,2,-3):
#     print(i)
# for i in range(15,2,-4):
#     print(i)


def binr(N):
    res = []
    for x in bin(N)[2:]:
        res.append(int(x))
    return res


def solution(N):
    # write your code in Python 3.6
    max = 0
    start = False
    i = 0
    s = binr(N)
    print(s)
    while i < len(s):
        if (s[i] == 1 )& (not start):
            temp = 0
            start = True
            i+=1
        elif s[i] == 0:
            temp += 1
            i+=1
        else:
            start = False
            if max < temp:
                max = temp
            

    return max
    pass

# print(solution(9))


def reverse_array(arr):
    size = len(arr)
    i=0
    print('array before:',arr)
    while i<(size//2):
        end = size-1-i
        arr[i], arr[end] = arr[end], arr[i]
        i+=1
    print('array after:',arr)


# a = [x for x in range(10)]
# b = [x for x in range(11)]
# reverse_array(a)
# reverse_array(b)
# print(10 in [1,2,3,10])

def rotate_by_K(A, K):
    # write your code in Python 3.6
    if (K == 0) | (len(A) == 0):
        return A
    K = K % (len(A))
    return A[len(A)-K:] + A[0:len(A)-K]


# a = [1, 2, 3, 4]
# rotate_by_K([], 5)

def pairs(A):
    # write your code in Python 3.6
    size = len(A)
    if size == 1:
        return A[0]

    A.sort()
    for i in range(0, size-1, 2):
        if A[i] != A[i+1]:
            return A[i]

####   LOOK at the next 2 algos #######

####this algo is O(n*n) because of dynamic array alloc
def solution(A):
    pre = []
    pos = []
    diff = []
    for x in A:
        if len(pre) == 0:
            pre.append(x)
        else:
            t = x + pre[-1]
            pre.append(t)

    for i in range(len(A)-1, -1, -1):
        if len(pos) == 0:
            pos.append(A[i])
        else:
            t = pos[0] + A[i]
            pos.insert(0, t)

    for j in range(len(pos)-1):
        diff.append(abs(pos[j+1]-pre[j]))
    diff.append(abs(pre[-2]-pos[-1]))

    return min(diff)

#### this algo is just O(N) because of pre-setting array size


def solution(A):

    pre = [0] * len(A)
    pos = [0] * len(A)
    diff = [0] * (len(A)-1)

    for k in range(len(A)):
        if k == 0:
            pre[k] = A[k]
        else:
            pre[k] = pre[k-1] + A[k]

    for i in range(len(A)-1, -1, -1):
        if i == (len(A)-1):
            pos[i] = A[i]
        else:
            pos[i] = pos[i+1] + A[i]

    for j in range(len(pos)-1):
        diff[j] = (abs(pos[j+1]-pre[j]))

    return min(diff)

# some bad cases this is O(N*M) where M=len(A) ->> pretty bad (better algo next)
def solution(N, A):
    # write your code in Python 3.6
    c = [0] * N
    maxi = 0
    for e in A:
        if e == (N+1):
            for i in range(len(c)):
                c[i] = maxi
        else:
            c[e-1] += 1
            if maxi < c[e-1]:
                maxi = c[e-1]

    return c
    pass

## complexity is O(n+m) wayyy better

def solution(N, A):
    # write your code in Python 3.6
    c = [0] * N
    maxi = 0
    maxi_all = 0
    for e in A:
        if e == (N+1):
            maxi_all = maxi
        else:
            if c[e-1] < maxi_all:
                c[e-1] = maxi_all + 1
            else:
                c[e-1] += 1

            if maxi < c[e-1]:
                maxi = c[e-1]

    for i in range(len(c)):
        if c[i] < maxi_all:
            c[i] = maxi_all

    return c
    pass

# L4 ex 3 to finish off!!!

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    c = [0] * (N+1)
    if(N == 1):
        if(A[0]!=1):
            return 1
        else:
            return 2

    for i in A:
        if (i > 0) & (i <= N) & (c[i] == 0):
            c[i] = 1

    for i in range(1, len(c)):
        if c[i] == 0:
            return i

    return len(c)
    pass


## L5 prob3 
def prefixe(A):
    pre = [0] * len(A)
    for i in range(len(A)):
        pre[i] = A[i] + pre[i-1]
    return pre


def slice_sum(P, i, j):
    return (P[j]-P[i-1])/((j-i)+1)


def solution(A):
    # write your code in Python 3.6
    pre = prefixe(A)
    mini = pre[-1]

    for i in range(len(A)-1):
        for j in range(len(A)-1, i, -1):
            if i == 0:
                avg = pre[j]/(j+1)
            else:
                avg = slice_sum(pre, i, j)

            if avg < mini:
                mini = avg
                start = i

    return start
    pass

# l5 prob genomics

def solutions(S, P, Q):

    a,c,g,t = 0,0,0,0
    
    A = [0] * (len(S)+1)
    C = [0] * (len(S)+1)
    G = [0] * (len(S)+1)
    T = [0] * (len(S)+1)

    res = [0] * len(P)
    for i in range(len(S)):
        if S[i]=='A':
            a+=1
            A[i+1]=a
        elif S[i]=='C':
            c+=1
            C[i+1]=c
        elif S[i]=='G':
            g+=1
            G[i+1]=g
        elif S[i]=='T':
            t+=1
            T[i+1]=t


    for j in range(len(P)):
        start = P[j]+1
        end = Q[j]+1

        if (start == end):
            if S[P[j]]=='A':
                res[j] = 1
            elif S[P[j]] == 'C':
                res[j] = 2
            elif S[P[j]]=='G':
                res[j] = 3
            elif S[P[j]] == 'T':
                res[j] = 4
            continue


        if(abs(A[start]-A[end])!=0):
            res[j]=1
        elif(abs(C[start]-C[end]) !=0):
            res[j] = 2
        elif(abs(G[start]-G[end])!=0):
            res[j]=3
        elif(abs(T[start]-T[end]) !=0):
            res[j] = 4
    
    return res


s = 'CAGCCTA'
p = [2,5,0]
q = [4,5,6]
solutions(s,p,q)

