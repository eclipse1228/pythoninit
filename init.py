#__init__ 미사용
class Businesscard:
    pass
    def set_info(self,name,email,addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("Name :",self.name)
        print("E-mail : ",self.email)
        print("Address : ",self.addr)

person1 = Businesscard()
person1.set_info("Bs","naver.com","Busan")
person1.print_info()              #("Bs","naver.com","Busan") 안 해도 됨 set_info에서 인스턴스에 값이 들어갔기 때문이다. 

-----------------------------------------------------------------------------------------------------------------------
#__init__ 사용
class Businesscard:
    pass
    def __init__(self,name,email,addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("Name:",self.name)
        print("E-mail: ",self.email)
        print("Address: ",self.addr)

member1 = Businesscard("Byeong Su","qudtnrh@naver.com","Busan") # class Businesscard에는 가 인자가 3개가 되야한다. __init__(self,name,email,addr)이기 때문에.. 
#아무것도 안 넣으면 오 ~ 류! ㅎㅎ..
member1.print_info() 

