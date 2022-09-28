from abc import ABC,abstractmethod
from factory_model.simple_factory_model import Chart,BarChart,PieChart

"""
需求：
开发一套图表库，该图表库可以为应用系统提供各种不同外观的图表，例如柱状图、饼状图。
新增需求1：
    增加折线图实现功能
"""

class LineChart(Chart):
    def __init__(self):
        print('折线图对象实例化')
    def display(self):
        print(f'draw linechart')

class ChartFactory(ABC):

    @abstractmethod
    def build_chart(self):
        pass

class BarChartFactory(ChartFactory):
    def __init__(self):
        self.obj = None
    def build_chart(self):
        self.obj = BarChart()
        return self.obj

class PieChartFactory(ChartFactory):
    def __init__(self):
        self.obj = None

    def build_chart(self):
        self.obj = PieChart()
        return self.obj

    @classmethod
    def build_chart_by_json(cls):
        print('解析JSON参数')
        return cls().build_chart()


class LineChartFactory(ChartFactory):
    def __init__(self):
        self.obj = None

    def build_chart(self):
        self.obj = LineChart()
        return self.obj

if __name__ == '__main__':
    obj = PieChartFactory.build_chart_by_json()
    obj.display()































