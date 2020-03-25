import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
s.connect(("localhost", 1234))
s.listen(1)
print("[+] Connction established")
print("[*] Sending message to Server..")
msg = input("Dein Nachricht: ")
try:
  pkg = msg.encode()
  s.send(pkg)
except:
  print("[!] Could not send message to Server!")
  s.close()
  quit()
print("[+] Messages have been sent!")
s.close()
