#模拟一下电脑装备的过程

class CPUFactory():
    def get_prod(self):
        print('获得一个CUP')

class MainBoardFactory():
    def get_prod(self):
        print('获得一个主板')

class MemoryFactory():
    def get_prod(self):
        print('获得一个内存')

class DiskFactory():
    def get_prod(self):
        print('获得一个硬盘')

class GPUFactory():
    def get_prod(self):
        print('获得一个显卡')

class PCBuider():
    def build_cpu(self):
        CPUFactory().get_prod()
    def build_gpu(self):
        GPUFactory().get_prod()
    def build_memory(self):
        MemoryFactory().get_prod()
    def build_mainboard(self):
        MainBoardFactory().get_prod()
    def build_disk(self):
        DiskFactory().get_prod()

class BuilderManager():
    class PC():
        def __init__(self):
            self.cpu = None
            self.gpu = None
            self.memory = None
            self.disk = None
            self.mainbord = None

    def get_pc(self):
        pc = self.PC()
        pc_b = PCBuider()

        pc.mainbord = pc_b.build_mainboard()
        print('1.主板安装')
        pc.cpu = pc_b.build_cpu()
        print('2.CPU安装')
        pc.memory = pc_b.build_memory()
        print('3.内存安装')
        pc.disk = pc_b.build_disk()
        print('4.硬盘安装')
        pc.gpu = pc_b.build_gpu()
        print('5.显卡安装')
        print('电脑组装完成')



if __name__ == '__main__':
    BuilderManager().get_pc()



























