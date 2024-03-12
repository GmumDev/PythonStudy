s = input()
cnt = [-1 for i in range(26)]

for i in range(len(s)):
    if cnt[ord(s[i]) - 97] == -1 :
        cnt[ord(s[i]) - 97] = i

for i in cnt:
    print(i, end=' ')