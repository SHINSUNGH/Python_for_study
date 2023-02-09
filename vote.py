



def str2int(votes):
    result = votes.split()
    # for i,item in enumerate(result):
    #     result[i] = int(item)
    result = list(map(int,result))
    return result

   
    pass

def countvotes(votes):
    n = max(votes)
    result = [ 0 for i in range(n)] # 컴프리헨션
    # for i in range(n):
    #     result.append(0)



    for item in votes:
        result[item-1] += 1
    return result
    
  


def printresult(reslut):
    for i, count in enumerate(reslut):
        print(f'기호 :  {1 + i : 2} 득표수 :  {count}')







votes = input("투표 번호 입력 : ")
result = str2int(votes)
print(result)
result = countvotes(result)
print(result)
printresult(result)