#함수명, 변수명 = 스네이크 케이스 이용 (_넣어서)
#클래스명 = 카멜 케이스 이용 (단어 첫글자를 대문자로)

# class BlackBox:
#     pass

# b1 = BlackBox()
# b1.name = '까망이'

# print(b1.name)
# print(isinstance(b1,BlackBox))

class Test:
    count = 0
    def __init__(self,age=7,*name) -> None:
        self.name = name
        self.age = age
        Test.count += 1
        self.count = Test.count

    def __str__(self) -> str:
        return f'test class[{self.name},{self.age},{self.count}]'



test01 = Test(7, '홍길동', '김철수')
print(type(test01))
print(test01)

# test02 = test('홍길동',22)
# test03 = test('박철우',21)
# print (test02.name,test02.age)
# test02.age = 34
# print (test02.name,test02.age)


# test02 = Test('홍길동',22)
# test03 = Test('박철우',21)
# Test.count += 1
# test02.count += 1
# Test.count += 1
# print (Test.count)
# print (test02.count)
# print (test03.count)

# test02 = Test('홍길동',22)
# test03 = Test('박철우',21)
# test04 = Test('박철',21)
# print (test02.count)
# print (test03.count)
# print (test04.count)