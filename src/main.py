from CYK import cyk_parse
from util import analyzing, splash, loading
from cfg_to_cnf import cfg_to_cnf
from input_converter import convert_input
import os


def main():
    loading("Loading")
    print()
    splash()
    print()
    running = True
    while running:
        grammar_path = "config/cfg.txt"
        filepath = input("Please input your text file path to check for syntax errors:\n")
        print()
        while not os.path.exists(filepath):
            reinput = input(
                "File does not exist. Would you like to input again? (y/n): "
            )
            if reinput.strip().lower() == "y":
                print()
                filepath = input(
                    "Please input your text file path to check for syntax errors:\n"
                )
                print()
            else:
                print()
                print("Goodbye!")
                exit()

        cnf_dict = cfg_to_cnf(grammar_path)
        with open(filepath, encoding="utf-8") as file:
            line = "".join(file.readlines())
            stream = convert_input(line)
        analyzing()
        print("Accepted.") if cyk_parse(stream, cnf_dict, stream) else print("Syntax error.")
        print()

        reinput = ""
        while reinput.strip().lower() != "y" and reinput.strip().lower() != "n":
            reinput = input("Would you like to check another file? (y/n): ")
            if reinput.strip().lower() == "n":
                print()
                print("Goodbye!")
                running = False
            else:
                print()


if __name__ == "__main__":
    main()
