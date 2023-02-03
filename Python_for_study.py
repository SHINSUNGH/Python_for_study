
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

# for i in range(2,10):
#     print ('\n -----', i, '단 -----')
#     for j in range(1,10):
#         print (i, '*', j, '=', i*j)



#     print ('2단',i)
# for j in range(3,27,3):
#     print ('        3단',j)
# for k in range(4,37,4):
#     print('                4단',k)


# for i in range(2,10):
#      print ('\n -----', i, '단 -----')
#      for j in range(1,10):
#          if j == 5: break
#          print (i, '*', j, '=', i*j)

# for i in range(2,10):
#      if (i%2) == 1: continue
     
#      print ('\n -----', i, '단 -----')
#      for j in range(1,10):
         
#       print (i, '*', j, '=', i*j)

# data = [1,2,3,4,5]
# while(data):
#     print(data.pop())

# while(1):
#     menu = input('1. 데이터 입력', '2.데이터 수정', '3.데이터 삭제','4.종료')
#     if menu == '1':
#         pass
#     elif menu == '2':
#         pass
#     elif menu == '3':
#         pass
#     elif menu == '4':
#         print ('프로그램 종료')
#         break


# import random;

# guess_number = random.randint(1,100)
# print ('1~100 중 숫자 맞춰보세요')
# users_input = int(input())
# while(users_input is not guess_number):
#     if users_input > guess_number:
#         print ("정답은 ", users_input, "보다 작습니다.")
#     else:
#         print ("정답은 ", users_input, "보디 큽니다.")
#     users_input = int(input())
# else:
#     print ("입력한 숫자 ", users_input, "정답입니다.")
    

# import random
# guess_num = random.randint(1~100)
# print ('숫자 맞추세요')
# users_num = int(input())
# while(users_num is not guess_num):
#     if users_num > guess_num:
#         print ("DOWN")
#     else:
#         print ("UP")
#     users_num = int(input())
# else:
#     print ("정답")


# import random
# guess_number = random.randint(1,100)
# print ('1~100 중 숫자 맞춰보세요')
# users_input = int(input())
# while(users_input is not guess_number):
#     if users_input > guess_number:
#         print ("정답은 ", users_input, "보다 작습니다.")
#     else:
#         print ("정답은 ", users_input, "보디 큽니다.")
#     users_input = int(input())
# else:
#     print ("입력한 숫자 ", users_input, "정답입니다.")

# import random
# num1 = random.randint(1,45)
# while int((num2 = num1)):
#     num  = random.randint(1,45):
# else:
#     print (num2)

# result = []

# for i in range(5):
#     import random
#     lotto = [0,0,0,0,0,0]
#     for x in range(6):
#         num = 0
#         while(num in lotto):
#             num = random.randint(1,45)
#         lotto[x] = num
#     lotto.sort()
#     result.append(lotto)
#     print (lotto)

#     print (result)

    # import random
    # lotto = [0,0,0,0,0,0]
    # while (num in lotto)
    #     num = random.randint(1,100)


# import random
# for i in range(5):
#     print(sorted(random. sample(range(1,46),6)))



import random
num = random. sample(range(1,31),3)
user_input_1 = int(input())
user_input_2 = int(input())
user_input_3 = int(input())
print (num)

    while ():
        if user_input_1 in num:
            print ("볼")
        if user_input_2 in num:
            print ("볼")
        if user_input_3 in num:
            print ("볼")