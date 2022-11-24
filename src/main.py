from cyk import cyk_parse
from util import (analyzing, splash, loading)

def main():
    loading("Loading")
    print()
    splash()
    print()
    path = input("Please input your text file path to check for syntax errors:\n")
    print()
    cnf = {
        'S' : ["AB", "BB"],
        'A' : ["CC", "AB", 'a'],
        'B' : ["BB", "CA", "b"],
        'C' : ["BA", "AA", "b"]
    }
    analyzing()

    print("Accepted.") if cyk_parse("aabb", cnf) else print("Syntax error.")

if __name__ == "__main__":
    main()