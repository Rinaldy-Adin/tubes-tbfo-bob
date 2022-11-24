import re
from finite_automata import finite_automata

_ALPHANUM = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + ["_"]
_KEYWORD = ["break", "const", "case", "catch", "continue", "default", "delete", "else", "false", "finally", "for", "function", "if", "let", "null", "return", "switch", "throw", "try", "true", "var", "while"]
_OPERATORS = [">>>=", "===", "!==", "<<=", ">>=", "**=", "&&=", "||=", "??=", ">>>","+=", "-=", "*=", "/=", "%=", "&=", "^=", "|=", "==", "!=", ">=", "<=", "++", "--", "**", "<<", ">>", "&&", "||", "??", "%", "+", "-", "*", "/" "=", ">", "<", "&", "|", "^", "~"]
_EXPANDS = ["(", ")", "{", "}", "[", "]", "?", ":", ",", ";"]


def convert_input(input_string):
  """Fungsi untuk mengubah string node js menjadi sebuah array"""
  # Mengidentifikasi string
  input_string = re.sub("\".*\"", " @varval ", input_string)

  # Mengidentifikasi semua operator
  for op in _OPERATORS:
    input_string = input_string.replace(op, " @operator ")

  # Memberikan spasi pada beberapa karakter
  for exp in _EXPANDS:
    input_string = input_string.replace(exp, " " + exp + " ")
  
  input_string = input_string.replace("\n", " ")
  input_string = input_string.split()

  for i in range(len(input_string)):
    str = input_string[i]
    if str not in _KEYWORD and str not in _EXPANDS and str[0] != '@':
      state = finite_automata(str)
      if state == "q2":
        input_string[i] = "@varval"
      elif state == "q3":
        input_string[i] = "@varval"

  return input_string

test_str2 = '''if (x == 0) {
  return 0
} else {
  return 1;
};

if (true) {
  return 23
} else if (false) {
  return "Mom en";
}
'''

print(convert_input(test_str2))