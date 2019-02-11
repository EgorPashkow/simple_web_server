class request_file:
    def __init__(self,request):
        self.headers = {}
        self.data = None
        self.parse(request)
    def parse(self,request):
        lines = request.split("\n\r")
        data = lines[0].replace("\n", " ").splitlines()
        for line in data:
            if not ":" in line:
                split = line.split(" ")
                self.set_headers("method",split[0])
                self.set_headers("path",split[1])
                self.set_headers("protocol",split[2])
                continue
            split_parameter = line.find(":")
            self.set_headers(line[:split_parameter+2],line[split_parameter+2:])
        if(len(lines)>1):
            self.data = str(lines[1]).replace("\n", " ")        
    def set_headers(self,key,value):
        self.headers[key] = value
    def get_headers(self,key):
        try:
            return self.headers[key]
        except KeyError:
            return ""