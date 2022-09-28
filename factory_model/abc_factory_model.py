from abc import ABCMeta,abstractmethod

"""
需求：
设计一套展示风格：
    春日风格
        -绿色按钮
        -绿色边框
        -绿色文本框
    夏日风格
        -蓝色按钮
        -蓝色边框
        -蓝色文本框
        
使用工厂方法面临的问题：
(1) 当需要增加新的皮肤时，虽然不要修改现有代码，但是需要增加大量类，针对每一个新增具体组件都需要增加一个具体工厂，
类的个数成对增加，这无疑会导致系统越来越庞大，增加系统的维护成本和运行开销。
(2) 由于同一种风格的具体界面组件通常要一起显示，因此需要为每个组件都选择一个具体工厂，用户在使用时必须逐个进行设置，
如果某个具体工厂选择失误将会导致界面显示混乱，虽然我们可以适当增加一些约束语句，但客户端代码和配置文件都较为复杂。   
"""

class Button(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass

class GreenButton(Button):

    def display(self):
        print(f'green button')

class BlueButton(Button):

    def display(self):
        print(f'blue button')

class Border(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass

class GreenBorder(Border):
    def display(self):
        print(f'green border')

class BlueBorder(Border):
    def display(self):
        print(f'blue border')

class Text(metaclass=ABCMeta):
    @abstractmethod
    def display(self):
        pass

class GreenText(Text):
    def display(self):
        print(f'green text')

class BlueText(Text):
    def display(self):
        print(f'blue text')

class Style(metaclass=ABCMeta):
    def creat_style(self):
        pass

class SpringStyle(Style):
    def creat_style(self):
        button = GreenButton().display()
        border = GreenBorder().display()
        text = GreenText().display()

class SummerStyle(Style):
    def creat_style(self):
        button = BlueButton().display()
        border = BlueBorder().display()
        text = BlueText().display()

if __name__ == '__main__':
    obj = SummerStyle()
    obj.creat_style()


















