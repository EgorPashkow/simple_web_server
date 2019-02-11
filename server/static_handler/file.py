class file:
    def __init__(self,path,base_directory):
        self.path = path
        self.base_directory = base_directory
        self.data = None
        self.expansion = None
        self.error = None
        try:
            self.read()
            self.get_expansion()
        except Exception as e:
            self.error = e.args
    def read(self):
        file = open("../" + self.base_directory + self.path,'rb')
        data = file.read()
        file.close()
        self.data = data
    def get_expansion(self):
        if "." in self.path:
            self.expansion = self.path.split('.')[1]