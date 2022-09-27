"""
需求：
开发一套图表库，该图表库可以为应用系统提供各种不同外观的图表，例如柱状图、饼状图。
"""
"""
典型的面向过程思维例子
step1
    step1.1
        step1.1.1
        step1.1.2
        step1.1.3
    step1.2
        step1.2.1
        step1.2.2
        
step2
    ...
step3
    ...

"""


class BarChart:
    def __init__(self):
        print('柱状图对象实例化')
    def draw_barchart(self):
        print(f'draw barchart')


class PieChart:
    def __init__(self):
        print('饼图对象实例化')

    def draw_piechart(self):
        print(f'draw pierchart')



class DrawChart():
    def __init__(self,name):
        self.name = name

    def display(self):
        if self.name == 'bar':
            # 这里可能是复杂的对象实例化过程
            bar = BarChart()
            bar.draw_barchart()

        elif self.name == 'pie':
            pie = PieChart()
            pie.draw_piechart()

        else:
            print('not support type')

if __name__ == '__main__':
    name = 'bar'
    chart = DrawChart(name)
    chart.display()













