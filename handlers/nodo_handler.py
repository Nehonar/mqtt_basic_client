import sys

def nodo_msg(msg):
  print(f"Received from topic: {msg['type']}\nMessage: {msg}")
  sys.stdout.flush()