class Person:
    def  __init__(self, name = None, age = None , address =None ):
        self.name = name
        self.age = age
        self.address = address
        self.hello = '안녕하세요.'
        print('Person__init__')
        # print('init쓰는법')
    def greeting(self):
        if self.name == None:
            print('이름을 입력하지 않았습니다.')
        else:
            print(f'안녕하세요. 저는 {self.name}입니다.')
        if self.age == None:
            print('나이를 입력하지 않았습니다.')
        else:
            print(f'저는 {self.age}살 입니다.')
        if self.address == None:
            print('주소를 입력하지 않았습니다.')s
        else:
            print(f'제 주소는 {self.address}입니다')

class Student(Person):
    def __init__(self):
    #     print('Student __ init__')
    #     super().__init__(self, name = None, age = None , address =None)