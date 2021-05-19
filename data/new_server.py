from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class webserverHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>Baba i praise you"
                output += "<form action='/hello' method='POST' enctype='multipart/form-data'><h1>What would you like me to say?</h1><input type='text' name='message'><input type='submit' value='Submit></form></body></html"                
                self.wfile.write(bytes(output, "utf8"))
                print(output)
                return

            if self.path.endswith("/holla"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body><h1>Baba Manshdhd</h1></body></html"
                output += "<form action='/hello' method='POST' enctype='multipart/form-data'><h1>What would you like me to say?</h1><input type='text' name='message'><input type='submit' value='Submit></form>"
                self.wfile.write(bytes(output, "utf8"))
                print(output)
                return
        except:
            self.send_error(404, 'File not Found')       

    def do_POST(self):
        try:
            self.send_response(301)
            self.end_headers()

            ctype, pdict = cgi.parse_header(self.headers['content-type'])
            pdict = bytes(pdict, "utf-8")
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                message = fields.get('message')

                output = ""
                output += "<html><body>"
                output += "<h2> How about this: "
                output += " <h1>{}vv</h1>".format(message)

                output += "<form action='/hello' method='POST' enctype='multipart/form-data'><h1>What would you like me to say?</h1><input type='text' name='message'><input type='submit' value='Submit> </form>"
                self.wfile.write(bytes(output, "utf8"))
        except:
            pass            


def main(server_class=HTTPServer, handler_class=webserverHandler):
    try:
        server_address = ('', 8000)
        httpd = server_class(server_address, handler_class)
        print('Web server running on port 8000')
        httpd.serve_forever()     
    except KeyboardInterrupt:
        print("^C pressed, stopping web server")
        httpd.socket.close()



if __name__ == '__main__':
    main()