#!/usr/bin/python

import BaseHTTPServer
import SocketServer
import RPi.GPIO as GPIO

PORT = 3004

GPIO.setmode(GPIO.PCM)
GPIO.setup( 23, GPIO.OUT)

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler)
  def do_HEAD(s):
    s.send_response(200)
    s.send_header("Content-type","text/html")
    s.end_headers()
  def do_GET(s):
    s.send_response(200)
    s.send_header("Content-type","text/html")
    s.end_headers()
    GPIO.output(23, GPIO.HIGH)
    sleep(1)
    GPIO.output(23, GPIO.LOW)


httpd = SocketServer.TCPServer(("0.0.0.0", PORT), MyHandler)

print "serving at port", PORT
httpd.serve_forever()




