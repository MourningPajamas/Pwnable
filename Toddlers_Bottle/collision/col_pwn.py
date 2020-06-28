from pwn import *

payload = p32(0x6c5cec8) * 4 + p32(0x6c5cecc)

connection = ssh('col', 'pwnable.kr', port=2222, password='guest')

p = connection.process(executable='./col', argv=['col', payload])

flag = p.recv().decode('utf-8')

print(f"Flag: {flag}")

connection.close()
