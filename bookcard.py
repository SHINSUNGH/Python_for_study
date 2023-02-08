# 도서관리 프로그램
# 데이터 구조는 리스트를 이용
# 일련번호, 책이름, 출판사, 

card = [['05830', '라플라스의 마녀', '히가시노 게이고', '(주)현대문학'],['77800', '오줌이 찔끔', '요시타케 신스케', '위즈덤하우스']]
while True:
    menu = input('''
    ------------------------------------------------------
                   실행할 작업을 선택하세요.
      1.저장, 2.수정, 3.삭제, 4.리스트, 5.검색, 6.종료(Q)
    ------------------------------------------------------
    ''')
    if menu == '1':
        while True:
            number = input('일련번호 입력 : ')
            check = 0
            for i in card:
                if i [0] == number:
                    check = 1
            if check == 0:
                break
            print('중복 번호 입니다. : ')
        bname = input('책 이름 입력 : ')
        author = input('저자 입력 : ')
        publisher = input('출판사 입력 : ')
        card.append([number, bname, author, publisher])
        print(card)
    elif menu == '2':
        number = input('수정할 도서의 일련번호 입력 : ')
        idx = -1
        for i, item in enumerate(card):
            if item[0] == number:
                idx = i
                update = int(input('수정할 정보를 고르세요  1.책 이름, 2.저자, 3.출판사'))
                card[idx][update] = input('수정내용 : ')
                break
            pass
    elif menu == '3':
        number = input('삭제할 책의 일련번호 입력 : ')
        delnum = 0
        for i in card:
            if i [0] == number:
                delnum = 1
            if delnum == 0:
                break
            print ('일련번호가 존재하지 않습니다.')
