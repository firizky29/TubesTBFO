# from copy import deepcopy
# import string
def readGrammar(filepath: str):
    try:
        with open(filepath, 'r') as f:
            grammar = f.read()
    except Exception as e:
        print("Caught exception: cannot open file <--- bakal di ganti")
        return
    lines = [line.split('->') for line in grammar.split('\n') if (len(line.split('->'))==2)]
    var = [line[0].replace(" ", "") for line in lines]
    prod = []
    for line in lines:
        terms = line[1].split('|')
        terms = [(((term.replace("or", "|")).replace("nl", "\n")).replace("sp", " ")).split() for term in terms]
        prod.append(terms)
    return dict(zip(var, prod))


# TODO : Debug CYK, debug grammer

'''  Di bawah ini adalah algoritma untuk debugging '''

# CFG = readGrammar("src/grammar/grammar.txt")
# for i, x in enumerate(CFG):
#     print(x, CFG[x])

# def isVariable(item):
#     if len(item) == 1:
#         return False
#     for char in item:
#         if char not in (string.ascii_uppercase + '_' + string.digits):
#             return False
#     return True

# def removeUnitProduction(CFG):
#     for variable in CFG:
#         productions = CFG[variable]
#         repeat = True
#         while repeat:
#             repeat = False
#             for production in productions:
#                 if len(production) == 1 and isVariable(production[0]):
#                     productions.remove(production)
#                     newProduction = deepcopy([production for production in CFG[production[0]]
#                                         if production not in productions])
#                     productions.extend(newProduction)
#                     repeat = True
#                     break
#     return CFG

# def updateToCNF(CFG):
#     newRule = {}
#     for variable in CFG:
#         terminals = []
#         productions = CFG[variable]
#         # Search terminals
#         processProduction = [production for production in productions if len(production) > 1]
#         for production in processProduction:
#             for item in production:
#                 if not(isVariable(item)) and item not in terminals:
#                     terminals.append(item)
#         # Create new rule and update production
#         for i, terminal in enumerate(terminals):
#             newRule.update({f"{variable}_TERM_{i + 1}": [[terminal]]})
#             for idx, j in enumerate(productions):
#                 if len(j) > 1:
#                     for k in range(len(j)):
#                         if len(productions[idx][k]) == len(terminal):
#                             productions[idx][k] = productions[idx][k].replace(terminal, f"{variable}_TERM_{i + 1}")
#         # Update productions so match A -> BC or A -> terminal
#         idx = 1
#         for i in range(len(productions)):
#             while len(productions[i]) > 2:
#                 newRule.update({f"{variable}_EXT_{idx}": [[productions[i][0], productions[i][1]]]})
#                 productions[i] = productions[i][1:]
#                 productions[i][0] = f"{variable}_EXT_{idx}"
#                 idx += 1
#     CFG.update(newRule)
#     return CFG

# def CFGtoCNF(CFG):
#     CFG = removeUnitProduction(CFG)
#     CNF = updateToCNF(CFG)
#     return CNF

# def printGrammar(dict):
#     for var in dict:
#         print(var,"-> ",end="")
#         for i in range(len(dict[var])):
#             if i == len(dict[var]) - 1:
#                 print(dict[var][i])
#             else:
#                 print(dict[var][i],"| ",end="")

# CFG = readGrammar("src/grammar/grammar.txt")
# CNF = CFGtoCNF(CFG)
# printGrammar(CNF)