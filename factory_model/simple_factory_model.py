from abc import ABCMeta,abstractmethod


class Chart(metaclass=ABCMeta):

    @abstractmethod
    def display(self):
        pass

class LineChart(Chart):
    def __init__(self):
        print('折线图对象实例化')
    def draw_linechart(self):
        print(f'draw linechart')


class BarChart(Chart):
    def __init__(self):
        print('柱状图对象实例化')
    def display(self):
        print(f'draw barchart')


class PieChart(Chart):
    def __init__(self):
        print('饼图对象实例化')
    def display(self):
        print(f'draw pierchart')

class ChartFactory:
    def __init__(self,name):
        self.name = name
        self.obj = None
    def get_chart(self):
        if self.name == 'bar':
            self.obj = BarChart()
        elif self.name == 'pie':
            self.obj = PieChart()
        else:
            print('not support type')
        return self.obj

class DrawChart():
    def __init__(self,name):
        self.name = name

    def display(self):
        obj = ChartFactory(self.name).get_chart()
        obj.display()


if __name__ == '__main__':
    name = 'bar'
    chart = DrawChart(name)
    chart.display()
    # obj = LineChart()
    # obj.display()