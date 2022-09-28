import threading
import time
#非线程安全的单例模式
class SingleTon():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            time.sleep(1) #模拟创建对象的耗时
            cls._instance =  super().__new__(cls,*args,*kwargs)
        return cls._instance



#线程安全的单例模式
class SingleTonThread():
    _instance = None
    _lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                time.sleep(1)
                cls._instance =  super().__new__(cls,*args,*kwargs)
            return cls._instance

def task():
    obj1 = SingleTon()
    obj2 = SingleTonThread()
    print(f'1:{id(obj1)}\n')
    print(f'2:{id(obj2)}')

if __name__ == '__main__':
    for i in range(2):
        t = threading.Thread(target=task)
        t.start()





















