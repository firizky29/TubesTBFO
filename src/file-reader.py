import string
def enumAtoms():
    with open('./src/grammar/syntax-atoms.txt', 'r') as f:
        lines = f.read()
    synatom = lines.split('\n')
    enum = dict(zip(synatom, [chr(ord('A')+i) for i in range(len(synatom))]))
    return enum



def read(filepath: str):
    try:
        with open(filepath, 'r') as f:
            w = f.read()
    except Exception as e:
        print("Caught exception: cannot open file <--- bakal di ganti")
        return

w = '''
1.2_2_212122_aklsdj_123
..1'''
# todo : ..1
# todo : ASJAKLSJ.123
# todo : .1231
# todo : 12312."asdasd"
# todo : var"asdasd"
alp = string.ascii_lowercase
Alp = string.ascii_uppercase
num = string.digits
res = ""
atom = enumAtoms()
while(w):
    # string processing
    if(w[0]=='\"'):
        tmp = w[1:]
        while(tmp):
            if(tmp[0]=='\n' or tmp[0]=='\"'):
                break
            tmp = tmp[1:]
        if(tmp):
            if(tmp[0]=='\n'):
                res += w[0]
            else:
                res += 's'
                w = tmp
        else:
            res += w[0]            
    elif(w[0] not in (alp+Alp+num+'_')):
        res += w[0]
    else:
        if(w[0] not in (alp+Alp+'_')):
            # cek floating point dan integer kemudian disubstitusi menjadi 'n'
            # cek ada var tidak valid, kemudian di assign menjadi 'x'
            if(w[0] in num):
                w = w[1:]
                while(w):
                    if(w[0] not in num):
                        break
                    w = w[1:]
                if(not w):
                    res += 'n'
                    break
                if(w[0]=='.'):
                    w = w[1:]
                    while(w):
                        if(w[0] not in num):
                            break
                        w = w[1:]
                    if(not w):
                        res += 'n'
                        break
                    if(w[0] in (alp+Alp+'_')):
                        w = w[1:]
                        while(w):
                            if(w[0] not in (alp+Alp+'_'+num)):
                                break
                            w = w[1:]
                        if(not w):
                            res += 'n.x'
                            break
                        res += 'n.x'+w[0]
                    else:
                        res += 'n'+w[0]
                elif(w[0] in (alp+Alp+'_')):
                    w = w[1:]
                    while(w):
                        if(w[0] not in (alp+Alp+'_'+num)):
                            break
                        w = w[1:]
                    if(not w):
                        res += 'x'
                        break
                    res += 'x'+w[0]
                else:
                    res += 'n'+w[0]
        else:
            cur = w[0]
            w = w[1:]
            while w:
                if(w[0] not in (alp+Alp+num+'_')):
                    break
                else:
                    cur += w[0]
                w = w[1:]
            if(cur in atom):
                if(w):
                    res += atom[cur]+w[0]
                else:
                    res += atom[cur]
            else:
                if(w):
                    res += 'v'+w[0]
                else:
                    res+='v'
    w = w[1:]
print(res)
    


