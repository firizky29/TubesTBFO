'''
Pseudocode, sumber: Wikipedia

let the wut be a string I consisting of n characters: a1 ... an.
let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
let P[n,n,r] be an array of booleans. Initialize all elements of P to false.

for each s = 1 to n
    for each unit production Rv → as
        set P[1,s,v] = true

for each l = 2 to n -- Length of span
    for each s = 1 to n-l+1 -- Start of span
        for each p = 1 to l-1 -- Partition of span
            for each production Ra    → Rb Rc
                if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true

if P[n,1,1] is true then
    I is member of language
else
    I is not member of language

'''

import numpy as np

def CYK(w: str, lang: dict):
    n = len(w) 
    m = len(lang)
    dp = np.zeros((m, n, n))
    id = dict(zip([i for i in range(m)], lang))
    rule = []
    i = 1
    for var in lang:
        rule.append(lang[var])
        i+=1
    for i in range(n):
        for j in range(m):
            for term in rule[j]:
                if(term[0]==w[i]):
                    dp[0][i][j] = True
    for l in range(1, n):
        for s in range(n-l+1):
            for p in range(l-1):
                for i in range(m):
                    for term in rule[i]:
                        if(len(term)!=1):
                            id1 = id[term[0]]
                            id2 = id[term[1]]
                            dp[l][s][i] = (dp[p][s][id1]&dp[l-p][s+p][id2])

    if(dp[n-1][0][0]):
        return -1
    else:
        lines = w.split('\n')
        idLines = dict(zip([i for i in range(len(w)) if w[i]=='\n'], [i for i in range(len(lines))]))
        ret = 1
        for i in range(n-1, -1, -1):
            if(dp[i][0][0]):
                break
            if(w[i]=='\n'):
                ret = idLines[i]
            return ret


