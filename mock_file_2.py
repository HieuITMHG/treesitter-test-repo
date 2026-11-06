from mock_file_1 import Student

hs1 = Student(name="Hieu", age=24)

def func_3(arr: list):
    for i in arr:
        print(i)

def do_something():
    hs1 = Student(name="Hieu", age=24)
    res = hs1.return_some_structure()
    print(res)
    func_3(res)
    return "hehe"

do_something()


