
# a = 300
# b = 300

# print (a is b)

# print (a == b)

# data_list = [1,2,3,4,5,[1,2,3]]
# print (data_list)
# print (len(data_list))
# print (len(data_list[-1]))

# print (min(data_list[-1]))
# print (max(data_list[-1]))

# print (count(data_list))

# data_1 = [3,56,7,2,5,6]
# data_1.sort()
# print (data_1)

# data_1.sort(reverse=True)
# print (data_1)

# data_1[0] = 10
# print (data_1)

# data_1 [1:3] = [2,2]
# print (data_1)

# data_1 [1:4] = [1,5,9,8,7,5,15]
# data_1.sort()
# del data_1 [:]
# print (data_1)


# data = [1,2,3]
# data.append(6)
# print (data)
# data.clear()
# print (data)

# data1 = [1,2,3]
# data2 = [4,5,6]
# data1.append(data2) #append = 문자열 리스트 자체를 넣어버림
# print (data1)
# data1.extend(data2) #extend = 리스트에 포함시킴
# print (data1)


# data1 = [1,2,3]
# data2 = [4,5,6]
# print (data1+data2)
# print (data1)

# data1.insert(0,6)
# print (data1)
# data1.remove(2)
# print (data1)
# a = data1.pop()

# print (a)

# data1.reverse
# print (data1)

# data1 = [1,2,3,4]
# data1.reverse()
# print (data1)

# t = 1,2,3
# a, b, c = t

# print (a)


# print ("Tell me your age?")
# myage = int(input('Tell me yout age \n'))
# if myage >= 20:
#     print ("Welcome to the Club")
# else:
#     print ("Get back your ass at home kid")

# print ("민증번호 13자리 까(ex : 123456-1234567" )

# mynum = input("민증번호 13자리 까(ex : 123456-1234567 \n" )
# if mynum[7] in ['1','3']:
#     mynum1 = '남자'
# else:
#     mynum[7] in ['2','3']
#     mynum1 = '여자'
# print (mynum[:6], mynum1)


# data = [1,2,3,4,5]
# for i in data:
#     print (i)

# for i in range(1,11,1):
#     print(i)

for i in range(2,10):
    print ('\n -----', i, '단 -----')
    for j in range(1,10):
        print (i, '*', j, '=', i*j)



#     print ('2단',i)
# for j in range(3,27,3):
#     print ('        3단',j)
# for k in range(4,37,4):
#     print('                4단',k)