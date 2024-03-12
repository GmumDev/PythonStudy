s = input().upper()
maxn = 0
maxc = ''
cntr = [0 for i in range(26)]
for i in s:
    cntr[ord(i) - 65] += 1

    if maxn < cntr[ord(i) - 65]:
        maxn = cntr[ord(i) - 65]
        maxc = i

    if maxc != i and maxn == cntr[ord(i) - 65]:
        maxc = '?'

print(maxc)