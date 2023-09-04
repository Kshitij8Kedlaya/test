class decode:
    def __init__(self,message,type):
        self.message = message
        self.type = type
    
    def inp(self):
        print(f"Decrypting {self.message}")
        print(f"The decoded message of the {self.type} cipher is:")

class reverse_cphr(decode):
    def msg(self):
        ansr = ''
        l = len(self.message) - 1
        while l >= 0: 
            ansr = ansr + self.message[l]
            l = l - 1
        print(ansr)

class caeser_cphr(decode):
    def msg(self):
        txt = ""
        for m in self.message:
            if m.isalpha():
                n = m.isupper()
                m = m.lower()
                dmsg = chr((ord(m) - 3))
                if n:
                    dmsg = dmsg.upper()
                txt += dmsg
            else:
                txt += m

        print(txt)


message = input("Enter the Secret Message: ")
print("reverse, caesar, ROT13")
type = input("Enter the type of cipher: ")

if type == "reverse":
    code1 = reverse_cphr(message,type)
    code1.inp()
    code1.msg()
elif type == 'caesar':
    code1 = caeser_cphr(message,type)
    code1.inp()
    code1.msg()




