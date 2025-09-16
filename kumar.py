from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
 <table border="8" cellpadding="9">
            <b>Device spacialisation(santhosh) </b>
          <tr bgcolor="pink">
            <td >s.no</td> 
            <td>name</td>
            <td>type</td>    
            
          </tr>
          <tr>
            <td>1.santhosh</td>
            <td>kavin</td>
            <td>dheena</td>

          </tr>
          <tr>
            <td cellpadding="2">2.kumar</td>
            <td>sakthi</td>
            <td>dibith</td>
          </tr>
          <tr>
            <td cellpadding="2" >3.guru</td>
            <td>sanjay</td>
            <td>sal</td>
            

<html>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()