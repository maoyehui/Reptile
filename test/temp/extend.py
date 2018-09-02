from pprint import pprint

class Base(object):
    def __init__(self):
        print('Base create')

class Basement(object):
    def __init__(self):
        print('Basement')

class childA(Base):
    def __init__(self):
        print('enter A')
        # Base.__init__(self)
        super(childA, self).__init__()
        print('leave A')

class childB(Base):
    def __init__(self):
        print('enter B')
        # Base.__init__(self)
        super(childB, self).__init__()
        print('leave B')

class childC(Basement):
    def __init__(self):
        print('enter C')
        super(childC, self).__init__()
        print('leave C')

class subClass(childA, childB, childC):
    def __init__(self):
        childA.__init__(self)
        childB.__init__(self)
        childC.__init__(self)

pprint(subClass.mro())
