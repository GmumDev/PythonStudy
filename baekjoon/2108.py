n = int(input())

a = []
sum = 0
dic = {}
choibin_list = []
choibin_cnt = 0
max = -4000
min = 4000
choibin_min = 4000
choibin_secmin = 4000
for i in range(n):
    inp = int(input())
    a.append(inp)
    sum += inp
    
    if inp in dic:
        dic[inp] += 1
    else:
        dic[inp] = 1
    
    if dic[inp] > choibin_cnt:
        choibin_cnt = dic[inp]
        choibin_list.clear()
        choibin_min = 4000
        choibin_secmin = 4000
        choibin_list.append(inp)
    elif dic[inp] == choibin_cnt:
        choibin_list.append(inp)
    
    max = inp if max < inp else max
    min = inp if min > inp else min
    if dic[inp] == choibin_cnt and inp < choibin_secmin:
        if inp < choibin_min:
            choibin_secmin = choibin_min
            choibin_min = inp
        else:
            choibin_secmin = inp

'''
산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.
'''

a.sort() ###

sansul = round(sum/n)
jungang = a[int((n-1)/2)]
bumwi = max - min

print(sansul)
print(jungang)
print(choibin_secmin if len(choibin_list) > 1 else choibin_min)
print(bumwi)

# n = 500,000.   3nlogn = 뻣는다. 

