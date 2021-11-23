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
    dp = np.zeros((n+1, n+1, m+1))
    id = dict(zip(lang, [i for i in range(1, m+1)]))
    rule = [None]
    for var in lang:
        rule.append(lang[var])

    for i in range(1,n+1):
        for j in range(1,m+1):
            for term in rule[j]:
                # print(term)
                if(term[0]=='__or__'):
                    tmp = '|'
                elif(term[0]=='__nl__'):
                    tmp = '\n'
                else:
                    tmp = term[0]
                if(tmp==w[i-1]):
                    dp[1][i][j] = True
                    break
                
    for l in range(2, n+1):
        for s in range(1, n-l+2):
            for p in range(1, l):
                for i in range(1, m+1):
                    for term in rule[i]:
                        if(len(term)!=1):
                            j = id[term[0]]
                            k = id[term[1]]
                            if(dp[p][s][j] and dp[l-p][s+p][k]):
                                dp[l][s][i] = True
                                break
                                
    if(dp[n][1][1]):
        return -1
    else:
        lines = w.split('\n')
        idLines = dict(zip([i for i in range(len(w)) if w[i]=='\n'], [i for i in range(len(lines))]))
        ret = 1
        for i in range(n, 0, -1):
            if(dp[i][1][1]):
                break
            if(w[i-1]=='\n'):
                ret = idLines[i-1]
        return ret




