#Текст → двоичные данные
text = "Hi!"
binary_text = ' '.join(format(ord(ch), '08b') for ch in text)
print(binary_text)

text = "Hello"
binary_text = ' '.join(format(ord(ch), '08b') for ch in text)
print(binary_text)

#Целые числа (integers)

print(bin(13))   # 0b1101

'''
Отрицательные числа

Компьютеры не хранят знак “–” как отдельный символ.
Они используют дополнительный код (two’s complement).

Принцип:

Берём двоичное число.

Инвертируем все биты (0 → 1, 1 → 0).

Прибавляем 1.

Пример: -5 в 8-битной системе
+5 = 00000101  
инвертируем → 11111010  
+1           → 11111011
'''

#Дробные числа (floating-point)
'''
Хранятся в формате IEEE 754 — специальный стандарт для float.

(–1)^sign × (1 + mantissa) × 2^(exponent – 127)

Расшифровка:

0 → знак “+”

10000001 → показатель степени (129 → значит 2^(2))

0111000... → дробная часть (0.4375)

'''
import struct

x = 5.75
# превращаем число в 4 байта (float32)
bits = struct.unpack('>I', struct.pack('>f', x))[0]
print(f"{x} → {bits:032b}")


# integer literals
'''
- variable
- literal

'''

a = 10 # 10 - Decimal integer literal
b = 0b10  # 0b10 - Binary integer literal
c = 0o10 # Octal
d = 0x10  # Hexadecimal


print(f'{a=}')
print(f'{b=}')
print(f'{c=}')
print(f'{d=}')

for n in range(16):
    print(f'dec: {n:8d} bin: {n:04b} oct: {n:8o} hex: {n:02X} ')
    pass

'''
dec:        0 bin: 0000 oct:        0 hex: 00
dec:        1 bin: 0001 oct:        1 hex: 01
dec:        2 bin: 0010 oct:        2 hex: 02
dec:        3 bin: 0011 oct:        3 hex: 03
dec:        4 bin: 0100 oct:        4 hex: 04
dec:        5 bin: 0101 oct:        5 hex: 05
dec:        6 bin: 0110 oct:        6 hex: 06
dec:        7 bin: 0111 oct:        7 hex: 07
dec:        8 bin: 1000 oct:       10 hex: 08
dec:        9 bin: 1001 oct:       11 hex: 09
dec:       10 bin: 1010 oct:       12 hex: 0A
dec:       11 bin: 1011 oct:       13 hex: 0B
dec:       12 bin: 1100 oct:       14 hex: 0C
dec:       13 bin: 1101 oct:       15 hex: 0D
dec:       14 bin: 1110 oct:       16 hex: 0E
dec:       15 bin: 1111 oct:       17 hex: 0F
'''

# Python bitwise operations
'''
Operator	Example	    Meaning
&	        a & b	    Bitwise AND
|	        a | b	    Bitwise OR
^	        a ^ b	    Bitwise XOR (exclusive OR)
~	        ~a	        Bitwise NOT
<<	        a << n	    Bitwise left shift
>>	        a >> n	    Bitwise right shift

'''


print("Bitwise operations:")
a = 0b1010
b = 0b1110
print(f'{a=:04b}\n{b=:04b}\n  {a&b:04b} -> a&b\n')
print(f'{a=:04b}\n{b=:04b}\n  {a|b:04b} -> a|b\n')
print(f'{a=:04b}\n{b=:04b}\n  {a^b:04b} -> a^b\n')
print(f'{a=:04b}\n  {~a:04b} -> ~a\n') # Two`s complement`
print(f'{a=:08b}\n  {a<<2:08b} -> a<<2\n') # 
print(f'{a=:08b}\n  {a>>2:08b} -> a>>2\n') # 

#standart bit manipulation 

import sys


a = True

print(sys.getsizeof(a))
'''
- get bit (get value of certain bit)
- set bit (set bit value to 1)
- clear bit (set bit in 0)
- toggle bit (invert bit)

'''

a = 0b0000000000000000000000001001
#                          6543210
print(sys.getsizeof(a))

def set_bit(val, bit_n): return val | (1 << bit_n)
def clear_bit(val, bit_n): return val & ~(1 << bit_n)
def get_bit(val, bit_n): return 1 & (val >> bit_n)
def toggle_bit(val, bit_n): return val ^ (1 << bit_n)

print(f'{a:08b}\n{set_bit(a, 1):08b}\n')
print(f'{a:08b}\n{clear_bit(a, 3):08b}\n')
print(f'{a:08b}\n{get_bit(a, 0)}\n')
print(f'{a:08b}\n{toggle_bit(a, 5):08b}\n')
b = toggle_bit(a, 5)
print(f'{a:08b}\n{toggle_bit(b, 5):08b}\n')
print()

a = 1<<5

print(f'{a:08b}')
'''


'''