#实现单例的其他方法

#类方法,该方法使用不当会出现问题，不建议工作中使用

class Myclass():
    _ins = None
    @classmethod
    def single_tone(cls):
        if cls._ins is None:
            cls._ins = cls.__new__(cls)
        return cls._ins



#装饰器方法
def single_tone(cls):
    _clss_list = {}
    def inner(*args,**kwargs):
        if cls not in _clss_list:
            _clss_list[cls]=cls(*args,**kwargs)
        return _clss_list[cls]
    return inner


@single_tone
class Test:
    def __init__(self):
        pass




if __name__ == '__main__':
    f1 = Myclass.single_tone()
    f2 = Myclass.single_tone()
    print(f1 == f2)
    f3 = Test()
    f4 = Test()
    print(f3 == f4)















