from CYK import cyk_parse
from util import analyzing, splash, loading
from cfg_to_cnf import cfg_to_cnf
from input_converter import convert_input
import os

def testing():
    grammar_path = "config/cfg.txt"
    test_files = ["test/test_const_acc.js", "test/test_const_rej.js", "test/test_func_acc.js", "test/test_func_rej.js", "test/test_switch_acc.js", "test/test_switch_rej.js", "test/test_if_acc.js", "test/test_if_rej.js", "test/test_for_acc.js", "test/test_for_rej.js", "test/test_try_acc.js", "test/test_try_rej.js", "test/test_while_acc.js", "test/test_while_rej.js"]

    cnf_dict = cfg_to_cnf(grammar_path)
    for file in test_files:
      print(file + " : ", end="")
      with open(file, 'r') as f:
        line = "".join(f.readlines())
        stream = convert_input(line)
      # print(stream)
      print("Accepted.\n") if cyk_parse(stream, cnf_dict, stream) else print("Syntax error.\n")

testing()
