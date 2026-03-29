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
        if isinstance(object, list) or isinstance(object, tuple):
            for i in object:
                self.pouch_contents.append(i)
        else:
            self.pouch_contents.append(object)
        return self
    
    def __add__(self, other):
        new_Kangaroo = Kangaroo()
        try:
            new_Kangaroo = self.pouch_contents + other.pouch_contents
            return new_Kangaroo
        except:
            return '大哥，你输入的是Kangaroo类嘛？'
    
a = Kangaroo()
a.put_in_pouch(2345)

b = Kangaroo([2, 4, 5])
print(a + b)