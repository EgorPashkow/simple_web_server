class response_file:
    def __init__(self):
        self.headers = {}
        self.data = None
    def prepare(self):
        headers = self.headers
        common = headers["protocol"] + " " + headers["status"]
        other = ""
        for key in headers:
            if(key == "protocol" or key == "status"):
                continue
            other += key + ":" + headers[key] + "\r\n"
        return str.encode(common + "\r\n" + other + "\r\n") + self.data
    def set_headers(self,key,value):
        self.headers[key] = value
    def get_headers(self,key):
        try:
            return self.headers[key]
        except KeyError:
            return ""
    def set_data(self,value):
        self.data = value
    def get_data(self):
        return self.data