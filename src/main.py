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
        # filepath = input("Please input your text file path to check for syntax errors:\n")
        filepath = "test/test_func_acc.txt"
        test_files = ["test/test_const_acc.txt", "test/test_const_rej.txt", "test/test_func_acc.txt", "test/test_func_rej.txt", "test/test_switch_acc.txt", "test/test_switch_rej.txt", "test/test_if_acc.txt", "test/test_if_rej.txt", "test/test_for_acc.txt", "test/test_for_rej.txt", "test/test_try_acc.txt", "test/test_try_rej.txt", "test/test_while_acc.txt", "test/test_while_rej.txt"]
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
        # for key, value in cnf_dict.items():
        #     print(key, ":", value)
        # with open(filepath, encoding="utf-8") as file:
        #     line = "".join(file.readlines())
        #     stream = convert_input(line)
        # print(stream)
        # # analyzing()
        # print("Accepted.") if cyk_parse(stream, cnf_dict, stream) else print("Syntax error.")
        # print()
        for file in test_files:
          print(file + " : ")
          with open(file, 'r') as f:
            line = "".join(f.readlines())
            stream = convert_input(line)
          # print(stream)
          print("Accepted.\n") if cyk_parse(stream, cnf_dict, stream) else print("Syntax error.\n")

        reinput = ""
        running = False
        # while reinput.strip().lower() != "y" and reinput.strip().lower() != "n":
        #     reinput = input("Would you like to check another file? (y/n): ")
        #     if reinput.strip().lower() == "n":
        #         print()
        #         print("Goodbye!")
        #         running = False
        #     else:
        #         print()


if __name__ == "__main__":
    main()
