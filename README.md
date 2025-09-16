# EX01 Developing a Simple Webserver
## Date:08.09.2025

## AIM:
To develop a simple webserver to serve html pages and display the Device Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```

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
```

## OUTPUT:

![alt text](<Screenshot (21).png>)
![alt text](<Screenshot (22).png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
