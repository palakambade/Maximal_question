def small(s):
    n = len(s)
    dist = max_distinct_char(s)
    minl = n

    for i in range(n):
        for j in range(n):
            sub = s[i:j]
            nsub = len(sub)
            sub_dist = max_distinct_char(sub)

            if (nsub < minl) and (dist == sub_dist):
                minl = nsub

    return minl

def max_distinct_char(s):
    count = [0]*256
    n = len(s)
    for i in range(n):
        count[ord(s[i])] +=1
    dist = 0
    for i in range(256):
        if count[i]!=0:
            dist += 1
    return dist

s = input("Enter String: ")
print(small(s))