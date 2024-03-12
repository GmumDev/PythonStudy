
testcase = int(input())

for t in testcase:
    n, targetIdx = map(int, input().split())

    #queue
    importancy = input().split()

    for i in range(n):
        importancy[i] = int(importancy[i])

    targetImportancy = importancy[i]
    
    #현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
    #나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 
    #이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 
    #그렇지 않다면 바로 인쇄를 한다.
    

