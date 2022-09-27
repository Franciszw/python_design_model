"""
1.元类type是用来生成类的，继承了元类的类，也具有生成类的功能了
2.一个类的生产默认使用type，如果不想使用type需要指明你使用的元类，因为类括号后面的使用非命名参数传递的都被认为是父类，指定元类只能使用命名参数
3.类名称加（）能生成对象是因为调用了元类的__call__方法
"""

class MyType(type):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance = None

    def __call__(self, *args, **kwargs):
        if not self.instance:
            self.instance = self.__new__(self)
            self.__init__(self.instance,*args,**kwargs)
        return self.instance

class SingleT(metaclass=MyType):
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def __str__(self):
        return f'name:{self.name}id:{self.id}'

f1 = SingleT('zw',1)
f2 = SingleT('sb',2)
print(f1 is f2)
print(f1)
print(f2)
























