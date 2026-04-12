class Kangaroo:
    def __init__(self, contents = []):
        self.pouch_contents = list()
        if isinstance(contents, list) or isinstance(contents, tuple):
            for i in contents:
                self.pouch_contents.append(i)
        else:
            self.pouch_contents.append(contents)
    
    def __str__(self):
        a = ''
        for i in self.pouch_contents:
            a += str(i) + ', '
        return a
    
    def put_in_pouch(self, object):
        if isinstance(object, (list, tuple)):
            for i in object:
                self.pouch_contents.append(i)
        else:
            self.pouch_contents.append(object)
        return self
    
    def __add__(self, other):
        try:
            for i in other.pouch_contents:
                self.pouch_contents.append(i)
            return self
        except:
            return '大哥，你输入的是Kangaroo类嘛？'
    
a = Kangaroo(1234)
a.put_in_pouch(5678)
b = Kangaroo((1,2,3,4))
b.put_in_pouch((5,6,7,8))

c = a + b
print(c)