class MathDojo(object):

    def __init__(self):
        self.results = 0

    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for v in i:
                    self.results += v
            else:
                self.results += i
        return self

    def subtract(self,*args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for v in i:
                    self.results -= v
            else:
                self.results -= i
        return self

    def result(self):
        print self.results
        return self

md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3]).result()

md2 = MathDojo()
md2.add(2).add(2,5).subtract(3,2).result()
