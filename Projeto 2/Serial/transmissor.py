#!/usr/bin/python3

from serial import Serial
import sys

try:
  porta = sys.argv[1]
except:
  print('Uso: %s porta_serial' % sys.argv[0])
  sys.exit(0)

try:
  p = Serial(porta, 9600, timeout=5)
except Exception as e:
  print('Não conseguiu acessar a porta serial', e)
  sys.exit(0)

f = open("file.txt","rb")
msg = f.read()
print(msg)

n = p.write(msg)
print('Enviou %d bytes' % n)

inp = input('Digite ENTER para terminar:')

sys.exit(0)