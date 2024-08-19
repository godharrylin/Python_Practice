from libs.base import Base

class ModuleA(Base):
    def __init__(self):
        super().__init__()
        self.name = 'Module A'


if __name__ == '__main__':
    mA = ModuleA.Run()