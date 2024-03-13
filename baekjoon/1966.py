
testcase = int(input())

for t in range(testcase):
    n, targetIdx = map(int, input().split())

    #queue
    importancy = input().split()

    for i in range(n):
        importancy[i] = int(importancy[i])

    
    #현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
    #나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
    #이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 
    #그렇지 않다면 바로 인쇄를 한다.

    cnt = 0
    while True:
        imp = importancy[0]
        if imp < max(importancy):
            importancy.append(imp)
            importancy.pop(0)
            if targetIdx == 0:
                targetIdx = len(importancy) - 1
            else:
                targetIdx -= 1
        else:
            cnt += 1
            if targetIdx == 0:
                print(cnt)
                break
            else: 
                targetIdx -= 1
                importancy.pop(0)
