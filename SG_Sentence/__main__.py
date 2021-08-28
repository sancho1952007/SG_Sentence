from SG_Sentence import *
option=input('1) Encode\n2) Decode\nEnter An Option: ')
if option=="1":
    enc=input('Enter Your Sentence: ')
    sg_encode(enc)
elif option=="2":
    dec=input('Enter Your Encoded Text: ')
    sg_decode(dec)
else:
    print('Please Enter A Valid Option')