morse = {'.-':'A','-...':'B','-.-.':'C','-..':'D',
'.':'E','..-.':'F','--,':'G','....':'H','..':'I',
'.---':'J','-.-':'K','.-..':'L','--':'M','-.':'N',
'---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S',
'-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
'-.--':'Y','--..':'Z','.----':'1','..---':'2',
'...--':'3','....-':'4','.....':'5','-....':'6',
'--...':'7','---..':'8','----.':'9','-----':'0',
}

class decode:
    def __init__(self,message,type):
        self.message = message
        self.type = type
    
    def inp(self):
        print(f"Decrypting {self.message}")
        print(f"The decoded message of the {self.type} cipher is:")

class reverse_cphr(decode):
    def msg(self):
        ans = ''
        l = len(self.message) - 1
        while l >= 0: 
            ans = ans + self.message[l]
            l = l - 1
        print(ans)

class caeser_cphr(decode):
    def msg(self):
        txt = ""
        dmsg = ''
        for m in self.message:
            if m.isalpha():
                n = m.isupper()
                o = m.lower()
                if m == 'a' or m == 'b' or m == 'c':
                    dmsg = chr((ord(m) + 23))
                elif n:
                    m = m.upper()
                    if m == 'A' or m == 'B' or m == 'C':
                        dmsg = chr((ord(m) + 23))
                    else:
                        dmsg = chr((ord(m) - 3))
                else:
                    dmsg = chr((ord(o) - 3))
                txt += dmsg
            else:
                txt += m

        print(txt)

class ROT13_cphr(decode):
    def msg(self):
        text = ""
        for m in self.message:
            if m.islower():
                if 'a' <= m <= 'm':
                    nmsg = chr(ord(m) + 13)
                elif 'n' <= m <= 'z':
                    nmsg = chr(ord(m) - 13)
            elif m.isupper():
                if 'A' <= m <= 'M':
                    nmsg = chr(ord(m) + 13)
                elif 'N' <= m <= 'Z':
                    nmsg = chr(ord(m) - 13)
            else:
                nmsg = m

            text += nmsg
        print(text)

class Morse_Code(decode):
    def msg(self):
        spl = self.message.split("   ")
        dcode = ''
        nc = ''
        for j in spl:
            j = j.upper()
            if j in morse:
                k = morse[j]
                nc += k
            else:
                nc = j
        dcode += nc
        print(dcode)


#Testcode = "ROT13- Uryyb Jbeyq, Reverse - !uoy teem ot eciN ,Caesar - L oryh Frglqj,Morse = .--.   -.--   -   ....   ---   -."

message = input("Enter the Secret Message: ")
while message:
    print("reverse, caesar, ROT13, Morse Code")
    type = input("Enter the type of cipher: ")
    if type == "reverse":
        code1 = reverse_cphr(message,type)
        code1.inp()
        code1.msg()
    if type == 'caesar':
        code1 = caeser_cphr(message,type)
        code1.inp()
        code1.msg()
    if type == 'ROT13':
        code1 = ROT13_cphr(message,type)
        code1.inp() 
        code1.msg()
        
    if type == 'Morse Code':
        code1 = Morse_Code(message,type)
        code1.inp() 
        code1.msg()
    message = input("Enter the Secret Message: ")
    
