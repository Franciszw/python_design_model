"""
假设现在又一个阅读器，目前支持txt和epub两种格式，现在需要增加一种新的格式支持，pdf
由于已经有现成的支持pdf相关的模块，所以考虑使用该模块来解决需求

目前的问题是：txt格式和epub格式在设计初期统一了接口阅读器面向接口编程，但是pdf模块的接口阅读器没法直接使用
"""
from adapter_model.third_pdfparser_model import PDFFormatParser
from abc import ABCMeta,abstractmethod
class FormatParser(metaclass=ABCMeta):
    @abstractmethod
    def func1(self):
        """
        获取文件
        :return:
        """
        pass
    @abstractmethod
    def func2(self):
        """
        解析文件
        :return:
        """
        pass


class TxtFormatParser(FormatParser):
    def func1(self):
        print('获取txt文件')

    def func2(self):
        print('解析txt文件')

class EpubFormatParser(FormatParser):
    def func1(self):
        print('获取epub文件')

    def func2(self):
        print('解析epub文件')

#pdf模块适配器

class PDFParserAdapter():
    def __init__(self):
        self.parser = PDFFormatParser()
    def func1(self):
        self.parser.func_a()
        self.parser.func_b()
        print('获取pdf文件')
    def func2(self):
        self.parser.func_d()
        self.parser.func_e()
        print('解析pdf文件')

class RederPlayer():

    def display(self,parser_cld):
        parser = parser_cld()
        parser.func1()
        parser.func2()
        print('展示文本')









if __name__ == '__main__':
    obj = RederPlayer().display(EpubFormatParser)









