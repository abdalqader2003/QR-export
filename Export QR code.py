import qrcode
from pystyle import *
print(Box.Lines('[+] Abood'))
Write.Print('[+] This program for Export QRcode\n\n',Colors.purple_to_blue,interval=0.1)
print(Box.DoubleCube('Export'))



name = Write.Input('Enter your name : ',Colors.red,interval=0.1)
age = Write.Input('Enter your age   : ',Colors.red,interval=0.1)
emp_info = name + age
qr = qrcode.make(emp_info)
Write.Print('waiting to generate qrcode \n ',Colors.green,interval=0.2)
save_name = Write.Input('Enter qrcode name to save : ',Colors.red_to_yellow,interval=0.2)
qr.save("D:\\" + save_name + ".jpg")


Write.Print('The qr code generated.....',Colors.blue,interval=0.1)
input('\n.........\n')