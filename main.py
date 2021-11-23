import sys
from src.CFGtoCNF import CFGtoCNF
from src.CYKalgorithm import CYK
from src.grammarreader import readGrammar
from src.filereader import read

def readLine(filepath, line) :
    lines = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
    lines[len(lines)-1] = lines[len(lines)-1] + "\n"
    return str(line+1)+ " | " + lines[line]

def displaycode(filepath) :
    lines = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
    idx = 1
    x = len(str(idx))+1
    for line in lines:
        for i in range(x-len(str(idx))):
            print(end=" ")
        print("   " + str(idx) + " |  " + line, end="")
        idx+=1

if __name__ == "__main__":
    print("===============================================================")
    print("                    PYTHON SYNTAX EVALUATOR")
    print("                  Made by : Kelompok 5 Kelas 2")
    print("===============================================================")

    CFG = readGrammar("src/grammar/grammar.txt")
    CNF = CFGtoCNF(CFG)

    if (len(sys.argv) < 2):
        fileinput = "src/tes.py"
    else:
        fileinput = sys.argv[1]
    try:
        inp = read(fileinput)
    except Exception:
        print()
        print(">> File " + str(fileinput) + " tidak dapat dibuka!")
        print(">> Membuka file src/tes.py ...")
        fileinput = "src/tes.py"
        inp = read(fileinput)
    
    print("\n>> Source Code")

    displaycode(fileinput)

    print("\n")
    print(">> Evaluating " + str(fileinput) + "...")
    print()

    x = CYK(inp, CNF)
    print(">> Hasil Evaluate")

    if x == -1 :
        print("   Accepted")
        print()
    else :
        print("   Syntax Error")
        print("   " + readLine(fileinput, x))
    print("===============================================================")