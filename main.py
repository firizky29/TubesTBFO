import sys
import os
from src.CFGtoCNF import CFGtoCNF
from src.CYKalgorithm import CYK
from src.grammarreader import readGrammar
from src.filereader import read

def readLine(filepath, line) :
    lines = []
    with open(filepath, 'r') as f:
        lines = f.readlines()
    return str(line+1)+ ". " + lines[line]

def find_files(filename, search_path):
    # Walking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result = os.path.join(root, filename)
    return result

if __name__ == "__main__":
    print("===============================================================")
    print("                    PYTHON SYNTAX EVALUATOR")
    print("                  Made by : Kelompok 5 Kelas 2")
    print("===============================================================")

    # grammar = find_files("grammar.txt", os.getcwd())
    # tes = find_files("tes.py", os.getcwd())
    # workdir = os.getcwd()

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
        exit

    print()
    print(">> Evaluating " + str(fileinput) + "...")
    print()

    x = CYK(inp, CNF)
    
    print(">> Hasil Evaluate")
    print()

    if x == -1 :
        print("Accepted")
        print()
    else :
        print("Syntax Error")
        print()
        print(readLine(fileinput, x))
    print("===============================================================")