from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocols</title>
</head>
<body>

    <h1>Available Protocols in TCP/IP</h1>

    <h2>1. Application Layer</h2>
    <ul>
        <li>HTTP</li>
        <li>HTTPS</li>
        <li>FTP</li>
        <li>SMTP</li>
        <li>DNS</li>
        <li>DHCP</li>
        <li>Telnet</li>
        <li>POP3</li>
        <li>IMAP</li>
    </ul>

    <h2>2. Transport Layer</h2>
    <ul>
        <li>TCP</li>
        <li>UDP</li>
    </ul>

    <h2>3. Internet Layer</h2>
    <ul>
        <li>IP</li>
        <li>ICMP</li>
        <li>ARP</li>
        <li>IGMP</li>
    </ul>

    <h2>4. Network Access Layer</h2>
    <ul>
        <li>Ethernet</li>
        <li>Wi-Fi</li>
        <li>PPP</li>
    </ul>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',880)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()