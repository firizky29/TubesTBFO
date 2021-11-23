from copy import deepcopy
import string
from grammar-reader import readGrammar

def isVariable(word):
    if len(word) == 1:
        return False
    for char in word:
        if char not in (string.ascii_uppercase + '_' + string.digits):
            return False
    return True

def removeUnitProduction(CFG : dict):
    for var in CFG:
        productions = CFG[var]
        repeat = True
        while repeat:
            repeat = False
            for production in productions:
                if len(production) == 1 and isVariable(production[0]):
                    productions.remove(production)
                    newProduction = deepcopy([production for production in CFG[production[0]] if production not in productions])
                    productions.extend(newProduction)
                    repeat = True
                    break
    return CFG

def updateToCNF(CFG : dict):
    newProduction = {}
    for var in CFG:
        terminals = []
        productions = CFG[var]
        # Mencari terminal
        processProduction = [production for production in productions if len(production) > 1]
        for production in processProduction:
            for item in production:
                if not(isVariable(item)) and item not in terminals:
                    terminals.append(item)
        # Membuat produksi baru
        for i, terminal in enumerate(terminals):
            newProduction.update({f"{var}_TERM_{i + 1}": [[terminal]]})
            for idx, j in enumerate(productions):
                if len(j) > 1:
                    for k in range(len(j)):
                        if len(productions[idx][k]) == len(terminal):
                            productions[idx][k] = productions[idx][k].replace(terminal, f"{var}_TERM_{i + 1}")
        # Mengubah produksi sehingga hanya ada A -> BC atau A -> terminal
        idx = 1
        for i in range(len(productions)):
            while len(productions[i]) > 2:
                newProduction.update({f"{var}_{idx}": [[productions[i][0], productions[i][1]]]})
                productions[i] = productions[i][1:]
                productions[i][0] = f"{var}_{idx}"
                idx += 1
    CFG.update(newProduction)
    return CFG

def CFGtoCNF(CFG : dict):
    CFG = removeUnitProduction(CFG)
    CNF = updateToCNF(CFG)
    return CNF

def display(grammar : dict):
    for var in grammar:
        print(var,"->",end=" ")
        for i in range(len(grammar[var])):
            if i == len(grammar[var]) - 1:
                print(grammar[var][i])
            else:
                print(grammar[var][i],"|",end=" ")

CFG = readGrammar('grammar.txt')
CNF = CFGtoCNF(CFG)
display(CNF)