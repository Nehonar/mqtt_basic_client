import sys

def gateway_msg(msg):
  print(f"Received from topic: {msg['type']}\nMessage: {msg}")
  sys.stdout.flush()