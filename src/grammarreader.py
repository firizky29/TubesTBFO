def readGrammar(filepath: str):
    try:
        with open(filepath, 'r') as f:
            grammar = f.read()
    except Exception as e:
        print("Caught exception: cannot open file")
        return
    lines = [line.split('->') for line in grammar.split('\n') if (len(line.split('->'))==2)]
    var = [line[0].replace(" ", "") for line in lines]
    prod = []
    for line in lines:
        terms = line[1].split('|')
        terms = [term.split() for term in terms]
        prod.append(terms)
    return dict(zip(var, prod))

