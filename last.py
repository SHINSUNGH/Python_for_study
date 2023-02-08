card = []

import json


with open('json_1.json','r') as f:
    card = json.load(f)

while True:
    menu = input('''
    ---------------------------------------------
    1.추가 2.수정 3.삭제 4.리스트 5.검색 6.종료(Q)
    ---------------------------------------------
    ''')
    if menu == '1':
        while True:
            name = input('이름 입력 : ')
            check = 0
            for item in card:
                if item['name'] == name:
                    check = 1
            if check == 0:
                break
            print('중복되는 이름이 있습니다.')
        address = input('주소 입력 : ')
        tel = input('전화번호 입력 : ')
        email = input('이메일 입력 : ')
        card.append({'name':name, 'address':address, 'tel':tel, 'email':email})
        print (card)
    elif menu == '2':
        name = input('수정할 이름을 입력해 주세요. : ')
        idx = -1
        for i, item in enumerate(card):
            if item['name'] == name:
                idx = i
                while True:
                    update = input('수정할 정보  address, tel, email, exit(종료) : ')
                    if update in ('address', 'tel', 'email'):
                        card[idx][update] = input(f'{update} 수정 내용 : ')
                    elif update == 'exit':
                        break
                print(card[idx])
                break
            if idx == -1:
                print('없는 데이터 입니다.')
    elif menu == '3':
        name = input ('삭제할 데이터의 이름을 입력해주세요 : ')
        delok = 0
        for i, item in enumerate(card):
            if item['name'] == name:
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
            -------------------------------------------------
            이름 : {item['name']}
            주소 : {item['address']}
            전화번호 : {item['tel']}
            이메일 : {item['email']}
            -------------------------------------------------
            ''')
        pass
    elif menu == '5':
        name = input('검색어를 입력해 주세요 : ')
        idx = -1
        for i, item in enumerate(card):
            if item['name'] == name:
                idx = i
                print(item)
                break
        if idx == -1:
            print ('데이터를 찾을 수 없습니다.')
        pass
    elif menu in ('6','q','Q','ㅂ'):
        with open('json_1.json','w') as f:
            json.dump(card,f,indent=2)
        print('프로그램 종료')
        break
    else:
        
        print('menu 선택을 잘못하셨습니다')
