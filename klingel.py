#!/usr/bin/python

import sys
import signal

import BaseHTTPServer
import SocketServer

import RPi.GPIO as GPIO
from time import sleep

PORT = 3004
IP = "0.0.0.0"

PIN = 23


# Server
class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_HEAD(s):
    s.send_response(200)
    s.send_header("Content-type","text/html")
    s.end_headers()
  def do_GET(s):
    s.send_response(200)
    s.send_header("Content-type","text/html")
    s.end_headers()
    GPIO.output(PIN, GPIO.HIGH)
    sleep(1)
    GPIO.output(PIN, GPIO.LOW)

# Mainloop
def main():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup( PIN, GPIO.OUT)

  httpd = SocketServer.TCPServer((IP, PORT), MyHandler)

  try:
    print "Server listening at ", IP,":", PORT
    httpd.serve_forever()
  finally:
    GPIO.cleanup()
    httpd.server_close()
    print("Server killed!")

# Signalhandler
def sigterm_handler(_signo,_stack_frame):
  print "SIGTERM received. Cleaning up..."
  sys.exit(0)

def sigint_handler(_signo,_stack_frame):
  print "SIGINT received. Cleaning up..."
  sys.exit(0)



if __name__ == '__main__':
  print "Starting klingelAPI..."
  signal.signal(signal.SIGTERM, sigterm_handler)
  signal.signal(signal.SIGINT, sigint_handler)
  main()
else:
  print "Run this script as __main__!"



