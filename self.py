#self 이해하기..
class Foo:
    def func1():
        print("function 1")

    def func2(self):
        print(id(self))
        print("function 2")
f = Foo()
f.func2()
print(id(f))
# 인자가 self뿌이므로 호출시 인자를 전달할 필요가없다.
# f.func1()  # 인자가 0이지만 1개를 받았다.라는 오류. ( 파이썬 메서드의 첫번째인자로 항상 인스턴스가 전달되기 때문이다.)

#f.func2()의 값 = id(f) 값
# 따라서 클래스내에서 정의된 self클래스는 인스턴스이다.
