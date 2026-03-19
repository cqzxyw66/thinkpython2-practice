import os

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print(path)
        else:
            walk(path)

def walk_new(dirname):
    d = list()
    for a, b, c in os.walk(dirname):
        if c != []:
            for names in c:
                print(os.path.join(a, names))
        else:
            for folders in b:
                print(f'{os.path.join(a, folders)}{'\\'}')

walk_new('D:\\SoftwareInstall\\NotepadPP')