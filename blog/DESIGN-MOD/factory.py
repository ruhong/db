#-*-coding:utf-8 -*-
#基类
class Person(object):
    def __init__(self):
        print "Hi, I am a person."

#子类
class Student(Person):
    def __init__(self):
        super(self.__class__, self).__init__()

if __name__ == "__main__":
    student = Student()
