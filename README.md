# EX01 Developing a Simple Webserver
## Date:16.11.2026
## REG NO:26018281

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

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
~~~

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

~~~


 OUTPUT:

![alt text](<Screenshot 2026-11-16 110139.png>)


![alt text](<Screenshot 2026-11-16 110207.png>)





## RESULT:
The program for implementing simple webserver is executed successfully.

