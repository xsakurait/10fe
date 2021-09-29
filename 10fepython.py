python 定数名　すべて大文字

 10進数に変える

２進数(バイナリ）　0bxx ８進数(オクテット）（ 0o(８の下をとったもの）xx 10進数0dxx １６（ヘキサ）0xxx　a=ob111 print(a)#7

print(bin(15)) #１０進数＞２進数へ　0b(bin)1111

print(oct(15))#１０進数＞８進数へ　0o(oct)17

print(hex(15))#１０進数>１６進数へ 0x(hex)f

a=complex(1,5)(実数部１虚数部３の複素数）

b=complex(2,4)

print(a,b)#(1,5) (2,4)

print(a+b)#(3+9j)

print(a-b)#(-1+1j)

print(a*b)#(2+20j)

print(a.real)#1.0(実数部表示

print(a.imag)#5.0(虚数部表示

a='apple'

print(a*10)#appleを１０回出力

b="""aplle

banana

grape

"""

print(b)#apple

             banana

             grape

encodeでバイナリ型に変更する

a.encode('utf-8')

print(type(a))#byte

decodeでバイナリ型から元に戻す

a.decode('utf-8')

a='abcABC'

b=a.upper()#すべて大文字にする

c=a.lower()#すべて小文字

d=a.swapcase()#大文字小文字変換

print(b,c,d)#ABCABC abcabc ABCabc

a='ABCDEABC'

print(a.replace('ABC','FFF',-1(デフォルト(すべて変換））(2だと左から２個変換）)#FFFDEFFF

b='abc'

print(b.capitalize())#最初の文字「a」だけ大文字に変換

