import os

class direction:
    def __init__(self,path,base_directory):
        self.path = path
        self.base_directory = base_directory
        self.data = None
        self.error = None
        try:
            self.read()
        except Exception as e:
            self.error = e.args
    def read(self):
        result = "<html><head><title>No index</title></head><body>"
        names = os.listdir("../" + self.base_directory + self.path)
        for name in names:
            result+="<a href='"+("../" + self.path + "/" + name)\
            .replace("//","/") + "'>" + name + "</a><br/>"
        result += "</body></html>"
        self.data = result.encode("utf-8")