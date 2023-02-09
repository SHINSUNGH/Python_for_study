import notebook as nb


note_1 = nb.Note('세상 사는 데 도움이 되는 명언')
note_2 = nb.Note('삶이 있는 한 희망은 있다')

notebook_1 = nb.NoteBook('명언노트')

notebook_1.add_note(note_1)
notebook_1.add_note(note_2)

print (notebook_1.get_number_of_pages)

import pickle

# with open ('note_data', 'rb' ) as f:
#     notebook = pickle.load(f)

    



import notebook as nb
notebook = None

with open ('note_save_data', 'rb' ) as f:
    notebook = pickle.load(f)

while True:
    menu = input('''
    ------------------------------------------------------------
     1.노트북 생성 2.내용 쓰기 3.노트 삭제 4.노트 내용 보기 5.종료
    ------------------------------------------------------------
    ''')
    
    if menu == '1':
        if notebook == None:
            notebook = nb.NoteBook(input('타이틀을 입력하세요 :'))
        else:
            print('생성된 노트북이 이미 있습니다.')

    elif menu == '2':
        if notebook == None:
            print('먼저 노트북을 생성해 주세요.')
        else:
            contents = input('노트 내용 입력 : ')
            note = nb.Note(contents)
            notebook.add_note(note)

    elif menu == '3':
        if notebook == None:
            print('노트북이 없습니다.')
        else:
            print(list(notebook.notes.keys()))
            page = int(input('page number : '))
            note = notebook.remove_note(page)
            print(note, ' 이(가) 삭제되었습니다.')

    elif menu == '4':
        if notebook == None:
            print('노트북이 없습니다.')
        else:
            print(list(notebook.notes.keys()))
            page = int(input('page number : '))
            ntoe = notebook.notes[page]
            print(note)

    elif menu == '5':
        with open('note_save_data', 'wb') as f:
            pickle.dump(notebook,f,protocol=pickle.HIGHEST_PROTOCOL)
            print('변경 내용을 저장하고, 프로그램을 종료합니다.')
        break


    else:
        print('없는 menu 입니다 다시 입력해 주세요.')