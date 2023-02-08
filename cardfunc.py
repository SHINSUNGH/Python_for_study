import json

card = []

def save(card):
    while True:
        name =input('이름을 입력해 주세요')
        check=0
        for item in card:
            if item['name']==name:
                check=1
        if check==0:
            break
        print( '중복되는 이름이 있습니다')
    adress= input('주소를 입력해 주세요')
    tel=input('전화번호를 입력해 주세요')
    email=input('이메일을 입력해 주세요')
    card.append({'name':name,'adress':adress,'tel':tel,'email':email})
    print(card)

def update(card):
    name == input ('수정 할 이름 ')
    idx = -1
    for i, item  in enumerate(card):
        if item ['name']==name:
            idx = i
        while True:
            update = input('수정할정보 address,tel ,email,exit(종료)')
            if  update in('address','tel' ,'email'):
                card[idx][update]=input(f'{update}수정할 내용 ')
                        
            elif update in ('q','Q','exit','6'):
                break
            print(card[idx])
            break

def delete():
    pass

def cardlist():
    pass

def search():
    pass

def datasave():
    pass

def dataload():
    pass












# card =[ {'name':'송승환','adress': '선화로10길 16','tel': '010-1234-4567','email': 'smg3333@naver.com'}
# ,{'name': '홍길동','adress': '동북로 10길 19','tel': '010-4567-4789','email' :'adjfkl1231@naver.com'}]
card=[]
with open('json_1.json','r') as f:
    card=json.load(f)



while True:
    menu= input('''
    -----------------------------------------------
    1저장 , 2수정, 3 삭제, 4리스트, 5검색 , 6종료(q),7(저장)
    ---------------------------------------------
    >>> ''')
    if  menu=='1':
        while True:
            name =input('이름을 입력해 주세요')
            check=0
            for item in card:
                if item['name']==name:
                    check=1
            if check==0:
                break
            print( '중복되는 이름이 있습니다')

        adress= input('주소를 입력해 주세요')
        tel=input('전화번호를 입력해 주세요')
        email=input('이메일을 입력해 주세요')
        card.append({'name':name,'adress':adress,'tel':tel,'email':email})
        print(card)
        
    elif menu =='2':
        name == input ('수정 할 이름 ')
        idx = -1
        for i, item  in enumerate(card):
            if item ['name']==name:
                idx = i
                while True:
                    update = input('수정할정보 address,tel ,email,exit(종료)')
                    if  update in('address','tel' ,'email'):
                        card[idx][update]=input(f'{update}수정할 내용 ')
                        
                    elif update in ('q','Q','exit','6'):
                        break
                
                print(card[idx])
                break
        if idx==-1:
            print('등록되지 않은 데이터 입니다')
    elif menu =='3':
        name =input("삭제할 이름 ")
        delok=0
        for i ,item in enumerate(card):
            if item['name']==name:
                print(item,"삭제!!")
                del card[i]
                delok =1
                break
            if delok==0:
                print("등록되지 않은 데이터 입니다")
        
    elif menu =='4':
        for item in card:
            print(f'''
            --------------------------------------
            이    름:{item['name']}
            주    소:{item['address']}
            전화번호:{item['tel']}
            이 메 일:{item['email']}
            
            ''')
    elif menu =='5':
        name=input('이름을 입력해 주세요 ')
        idx=-1
        for i ,item in enumerate(card):
            if item['name'] ==name:
                idx =i 
                print(item)
                break
        if idx== -1:
            print('등록되지 않은 데이터 입니다 ')
    elif menu in('6','q','Q'):
        print('저장중...')
        
        print('프로그램 종료 ')
        with open ('json_1.json.txt','w') as f:
            json.dump(card,f,indent=2)
        break
        
            


    
    else :
        print(' 메뉴 선택을 잘못 하셨습니다')
    
    
    

