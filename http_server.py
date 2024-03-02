from http.server import HTTPServer, BaseHTTPRequestHandler
import json
IP=80
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond to a GET request with a simple message
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Server is up and running!')



    def do_OPTIONS(self): 
        self.send_response(200, "ok")       
        self.send_header('Access-Control-Allow-Origin', '*')                
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type") 
        #self.send_header("Access-Control-Allow-Headers", "X-Requested-With")    
        self.end_headers()


    def do_POST(self):
        # Read the data sent with the POST request
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))

        # Extract the relevant information from the data
        message = data['message']
        answer = data['answer']
        user_ip = data['userIP']
        port = data['port']
        time = data['time']
        import datetime
        # Get the current date and time
        now = datetime.datetime.now()
        # Format the date and time as desired
        date_time = now.strftime("%Y-%m-%d")
        # Print the formatted date and time
        #print("Current date and time:", date_time)
        # Open a log file for writing
        # Write the information to a log file
        with open('./log/'+date_time+'log.txt', 'a') as f:
            f.write(f"Message: {message}\n")
            f.write(f"Answer: {answer}\n")
            f.write(f"User IP: {user_ip}\n")
            f.write(f"Port: {port}\n")
            f.write(f"Time: {time}\n")
            f.write("\n")

        # Respond to the POST request with a success message
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Successfully received data and saved to log file!')

# Start the server and run forever
with HTTPServer(('0.0.0.0', IP), RequestHandler) as httpd:
    print("Serving forever on port %s..."%str(IP))
    httpd.serve_forever()
