import os

def enumAtoms():
    with open('./src/grammar/syntax-atoms.txt', 'r') as f:
        lines = f.read()
    synatom = lines.split('\n')
    enum = zip(synatom, [chr(ord('A')+i) for i in range(len(synatom))])
    return enum


