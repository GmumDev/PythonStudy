n = int(input())
scores = input().split()
for i in range(n):
    scores[i] = int(scores[i])

mx = max(scores)
sum = 0
for i in range(n):
    scores[i] = scores[i]/mx*100
    sum += scores[i]

print(sum/n)