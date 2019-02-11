from response import response_file
from static_handler.file import file
from static_handler.direction import direction
import static_handler.utils as utils

class request_handler:
    def __init__(self):
        self.working_directory = "directory"
    def hand(self,request):
        path = request.get_headers("path")
        response = response_file()
        response.set_headers('protocol',"HTTP/1.1")
        response.set_headers('Connection',"close")
        files = file(path,self.working_directory)
        if not files.error == None:
            if not path.endswith("/"):
                path = path + "/"
            files = file(path + "index.html",self.working_directory)
            if not files.error == None:
                files = file(path + "index.htm",self.working_directory)
        if files.error == None:
            response.set_headers("status","200 OK")
            response.set_headers("Content-Type",utils.get_exp(files.expansion))
            response.set_data(files.data)
        else:
            response.set_headers("status","404 Not found")
            response.set_data(b"404 Not found")
            if((path.endswith("/") and not path == "/") or
               path.find(".") == -1):
                direction2 = direction(path,self.working_directory)
                if not direction2.error == None:
                    response.set_headers("status","404 Not found")
                    response.set_data(b"404 Not found")
                else:
                    response.set_headers("status","200 OK")
                    response.set_data(direction2.data)
            if path == "/":
                response.set_headers("status","200 OK")
                response.set_data(direction("",self.working_directory).data)
        return response.prepare()