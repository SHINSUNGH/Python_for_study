
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



# import random
# num = random. sample(range(1,31),3)
# user_input_1 = int(input())
# user_input_2 = int(input())
# user_input_3 = int(input())
# print (num)

#     while ():
#         if user_input_1 in num:
#             print ("볼")
#         if user_input_2 in num:
#             print ("볼")
#         if user_input_3 in num:
#             print ("볼")

# count = 0

# while True:             # 플레이어가 정답을 맞추기 전까지 계속 반복
#     strike = 0 
#     ball = 0      # 입력 할 때마다 스트라이크, 볼 값은 계속 바뀜
#     user = input("세 숫자를 입력하세요: ")
#     try:          # 플레이어가 세 숫자가 아닌 다른것을 입력 할 때 예외처리
#         if len(user) != 3:
#             raise ValueError # 숫자가 세자리가 아니면 ValueError 발생시킴

#         f = int(user[0])
#         s = int(user[1])
#         t = int(user[2])        #수 비교를 위해 type을 정수형(int)으로 변환

#         if f == s or f == t or s == t:
#             raise ValueError # 중복되는 숫자를 입력할시 ValueError 발생시킴

#     except ValueError:                   # ValueError발생시 실행할 코드
#         print("다시 입력하세요")
#         continue

#     print("입력한 숫자는 {}입니다".format(user))

#     if f == answer[0]:
#         strike += 1
#     elif f == answer[1] or f == answer[2]:
#         ball += 1

#     if s == answer[1]:
#         strike += 1
#     elif s == answer[0] or s == answer[2]:
#         ball += 1

#     if t == answer[2]:
#         strike += 1
#     elif t == answer[0] or t == answer[1]:
#         ball += 1                           # 하나하나 비교하며 스트라이크 볼 판단

#     if strike != 3:
#         print("{} 스트라이크, {} 볼 입니다".format(strike, ball))
#         count += 1 # 한번 입력할 때마다 카운트 1씩 증가
#     elif strike == 3: 
#         count += 1
#         break # 3스트라이크면 반복문 탈출

# print("{} 정답입니다. {}번만에 맞추셨습니다.".format(user, count))

# import random

# com = random.sample(range(1,10) ,3)
# print (com)

# strike = 0
# count = 0
# print ('시작')

# while strike != 3:
#     strike = 0
#     ball = 0
#     guess = list(input("3자리 숫자를 입력하세요"))
#     print (guess)
#     for  a in  guess:
#         for b in com:
#             if int(a) == b:
#                 if guess.index(a) == com.index(b):
#                     strike += 1
#                 else:
#                     ball += 1
    
#     count += 1
#     print ("strike : ", strike, "볼 : ", ball, "시도 횟수 : ", count)
# print ("정답")



# import random
# count = 0
# oper = [ '+', '-', '*', '/' ]
# for x in range(5):
#     a = random.randint(1,50)
#     b = random.randint(1,50)
#     op = oper [random.randint(0,3)]
#     print (a , op, b)
#     answer = int(input("정답"))
#     result = 0
#     if op == '+':
#         result = a + b
#     elif op == '-':
#         result = a - b
#     elif op == '*':
#         result = a * b
#     elif op == ('/'):
#         result = a // b
#     if answer == result:
#         print ('정답')
#         count += 1
#     else:
#         print ('오답')

# print (count, '개 맞음')


# import random
# count = 0
# oper = [ '+', '-', '*', '/' ]
# for x in range(5):
#     a = random.randint(1,50)
#     b = random.randint(1,50)
#     op = random.choice(oper)
#     print (a , op, b)
#     answer = int(input("정답"))
#     result = 0
#     if op == '+':
#         result = a + b
#     elif op == '-':
#         result = a - b
#     elif op == '*':
#         result = a * b
#     elif op == ('/'):
#         result = a b
#     if answer == result:
#         print ('정답')
#         count += 1
#     else:
#         print ('오답')

# print (count, '개 맞음')


# a = 'abcdefg'
# print (a[:])
# print (len(a))

# b = 'Qwer x asdf'
# print (b.upper())
# print (b.split(), b.lower())
# print (b.count('f'))
# print (a.find('c'))
# print (b.startswith('Q'))
# print (b.startswith('q'))
# print (a.count('d', 0, 4))

# import random
# oper = ['+','-','*','/']
# count = 0
# for x in range(5):
#     a = random.randint(1,10)
#     b = random.randint(1,10)
#     op = random.choice(oper)
#     quiz = str(a) + op + str(b)
#     print (quiz, '=')
#     answer = ''
#     while not answer.isdigit():
#         answer = input ('정답')
#     answer = input(answer)
#     resulte = 0
#     if answer == int(eval(quiz)):
#         print ('정답')
#         count += 1
#     else:
#         print ('오답')
#     print (count, '개 맞음')


# a = input()
# b = 'asd %s asd' (%a)
# print (b)

# a = 30
# b = 'asd'

# print(f'sadwa {a} asdf {b} asd')

# name = input('이름 입력')
# age = input('나이 입력')

# print (f'이름 : {name} 나이 : {age} 세 맞습니까?


# information = {'name':'신성혁', 'age':'25'}

# print (information['name'])
# print (information)
# information['address'] = '충주'

# print (information)

# print (information)

# print (information)

# print (information.keys())

# print (information.values())

# print (information.items())

# print (information.get('name'))

# print ('name' in information)

# print ('신성혁' in information)

# Business_card = {'name':'신성혁', 'address':'만리산 10길 28', 'email':'shin1235631@gmail.com'}

# while True:
#     menu = input('''
#     ---------------------------------------------
#     1.저장 2.수정 3.삭제 4.리스트 5.검색 6.종료(Q)
#     ---------------------------------------------
#     ''')
#     if menu == '1':
#          print('''
         
#          ''')
#          if input = 1
#             print('''
#             어떤 정보를 저장 하시겠습니까?
#             ----------------------
#             1.이름 2.주소 3.이메일
#             ----------------------
#             ''')
#         if input = '1'
            
#         pass
#     elif menu == '2':
#         pass
#     elif menu == '3':
#         pass
#     elif menu == '4':
#         pass
#     elif menu == '5':
#         pass
#     elif menu == '6':
#         print('프로그램 종료')
#         break
#     else:
#         print('menu 선탹을 잘못하셨습니다')
card = [['신성혁', '충주', '010-3650-3437', 'shin1575631@gmail.com'],
        ['신성주', '충주', '010-7550-9730', 'ssj@gmail.com']]
while True:
    menu = input('''
    ---------------------------------------------
    1.저장 2.수정 3.삭제 4.리스트 5.검색 6.종료(Q)
    ---------------------------------------------
    ''')
    if menu == '1':
        while True:
            name = input('이름 입력 : ')
            check = 0
            for item in card:
                if item[0] == name:
                    check = 1
            if check == 0:
                break
            print('중복되는 이름이 있습니다.')
        address = input('주소 입력 : ')
        tel = input('전화번호 입력 : ')
        email = input('이메일 입력 : ')
        card.append([name, address, tel, email])
        print (card)
    elif menu == '2':
        name = input('수정할 이름을 입력해 주세요. : ')
        idx = -1
        for i, item in enumerate(card):
            if item[0] == name:
                idx = i
                update = int(input('수정할 정보(1.address, 2.tel, 3.email'))
                card[idx][update] = input('수정 내용 : ')
                print (card[idx])
            break
        pass
    elif menu == '3':
        name = input ('삭제할 데이터의 이름을 입력해주세요 : ')
        delok = 0
        for i, item in enumerate(card):
            if item[0] == name:
                print (item, ' 삭제 되었습니다.')
                del card[i]
                delok = 1
                break
            if delok == 0:
                print('이름을 찾을 수 없습니다.')   
        pass
    elif menu == '4':
        for item in card:
            print (f'''
            ---------------------------------------------------
            이름 : {item[0]}
            주소 : {item[1]}
            전화번호 : {item[2]}
            이메일 : {item[3]}
            ---------------------------------------------------
            ''')
        pass
    elif menu == '5':
        name = input('검색어를 입력해 주세요 : ')
        idx = -1
        for i, item in enumerate(card):
            if item[0] == name:
                idx = i
                print (f'''
            ---------------------------------------------------
            이름 : {item[0]}
            주소 : {item[1]}
            전화번호 : {item[2]}
            이메일 : {item[3]}
            ---------------------------------------------------
            ''')
            break
        if idx == -1:
            print ('데이터를 찾을 수 없습니다.')
        pass
    elif menu in ('6','q','Q'):
        print('프로그램 종료')
        break
    else:
        print('menu 선택을 잘못하셨습니다')

# f = open('test.txt','r',encoding='utf8')
# text = f.read()
# print (text)
# a.close()

# with open('test.txt','r',encoding='utf8') as f:
#     while True:

#         text = f.readline()
#         if not text:
#             break
#         print(text)


# with open ('test_w.txt', 'w',encoding='utf8') as f:
#     f.write('\n배가 나을 기미가 안보여요유ㅠㅠㅠ')

# # import pickle
# card = [{'name':'신성혁', 'address':'충주', 'tel' : '010-3650-3437', 'email':'shin1575631@gmail.com'},
#         {'name':'신성주', 'address':'충주', 'tel' :'010-7550-9730', 'email':'ssj@gmail.com'}]

# f = open('pickle', 'wb')
# pickle.dump(card,f)
# f.close()

# import pickle
# with open('pickle', 'wb') as f:
#     data = pickle.load(f)

#     print (data)

# import json
# with open('jsontest.json','w') as f:
#     json.dump(card,f,indent=2)

# import json
# with open('jsontest.json','w') as f:
#     data = json.load(f)
#     print(type(data))
#     print(data)


# def ftl(n):
#     if n == 1:
#         return 1
#     else:
#         return n * ftl(n - 1)
# print (ftl(int(input("Input number for Factorial : "))))

# def add(a=2,b=3):
#     return a + b


# print (add(10))

# def add(*a):
#     check = 0
#     for i in a:
#         check += i
#     return check

# print (add(1,2,3,4,5,6,7,8,9))

def add(**a):
    print(a)

print(add(a=1,b=2,c=3))2