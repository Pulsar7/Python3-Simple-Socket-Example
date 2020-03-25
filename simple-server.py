import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
s.bind(("localhost", 1234))
s.listen(1)
(client,addr) = s.accept()
print("[+] Connction established to %s"%(str(addr)))
print("[*] Receiving message from Client..")
try:
  pkg = client.recv(2048)
  msg = pkg.decode()
except:
  print("[!] Could not receive message from Client!")
  client.close()
  s.close()
  quit()
print("[+] Received : %s"%(str(msg)))
client.close()
s.close()
