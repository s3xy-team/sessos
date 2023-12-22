from pwn import *

r = process('./PiovegoRecipe')

r.sendline(b'Patate-Prezzemolate')
r.sendline(b'56')
r.sendline(b'123')
r.sendline(b'Swe4T')
r.interactive()
