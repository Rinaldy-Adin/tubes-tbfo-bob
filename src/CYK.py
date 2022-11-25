from tabulate import tabulate

def cyk_parse(word, cnf, header):
# Returns True for Accept, False for Reject
    n = len(word)
    if n == 0:
        return False
    
    table = [[set([]) for j in range(n)] for i in range(n)]
    for i in range(n):
        for left, right in cnf.items():
            for product in right:
                for idx, elmt in enumerate(word):
                    if product[0] == elmt:
                        table[idx][idx].add(left)

    for l in range(1, n):
        for i in range(n-l):
            j = i+l
            for k in range(i, j):
                for left, right in cnf.items():
                    for product in right:
                        if len(product) == 2 and product[0] in table[i][k] and product[1] in table[k+1][j]:
                            table[i][j].add(left)

    # for lines in table:
    #     print(lines)

    # FOR DEBUGGING
    # for idx, lines in enumerate(table):
    #     lines.insert(0, header[idx])
    # f = open("out.txt", "w")
    # f.write(tabulate(table, headers=header, tablefmt="github"))

    # FOR DEBUGGING
    # if 'S' in table[0][n]:
    #     return True
    # else:
    #     return False


    if 'S' in table[0][n-1]:
        return True
    else:
        return False
