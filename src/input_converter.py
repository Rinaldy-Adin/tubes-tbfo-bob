import re
from finite_automata import finite_automata

_KEYWORD = ["break", "const", "case", "catch", "continue", "default", "delete", "else", "false", "finally", "for", "function", "if", "let", "null", "return", "switch", "throw", "try", "true", "var", "while"]
# _OPERATORS = [">>>=", "===", "!==", "<<=", ">>=", "**=", "&&=", "||=", "??=", ">>>","+=", "-=", "*=", "/=", "%=", "&=", "^=", "|=", "==", "!=", ">=", "<=", "++", "--", "**", "<<", ">>", "&&", "||", "??", "%", "+", "-", "*", "/" "=", ">", "<", "&", "|", "^", "~"]
_ASSIGNMENT_OPERATORS = [">>>=", "!==", "<<=", ">>=", "**=", "&&=", "||=", "??=", "+=", "-=", "*=", "/=", "%=", "&=", "^=", "|="]
_UNARY_OPERATORS = ["++", "--", "~"]
_BINARY_OPERATORS = ["===", "!==", "==", "!=", ">=", "<=", "**", "<<", ">>", "&&", "||", "??", "%", "+", "-", "*", "/", ">", "<", "&", "|", "^"]
_EXPANDS = ["(", ")", "{", "}", "[", "]", "?", ":", ",", ";", "."]
_SPECIALS = ["="]


def convert_input(input_string):
  """Fungsi untuk mengubah string node js menjadi sebuah array"""
  # Menghilangkan comment
  input_string = re.sub("/[*].*[*]/", "", input_string)
  input_string = re.sub("//.*\n", "", input_string)

  # Mengidentifikasi string
  input_string = re.sub("\".*?\"", " @value ", input_string)

  # Mengidentifikasi array
  input_string = re.sub("\[.*\]", " @value ", input_string)

  # # Mengidentifikasi semua operator
  # for op in _OPERATORS:
  #   input_string = input_string.replace(op, " @operator ")

  # Mengidentifikasi assignment operator
  for op in _ASSIGNMENT_OPERATORS:
    input_string = input_string.replace(op, " @assign_op ")

  # Mengidentifikasi unary operator
  for op in _UNARY_OPERATORS:
    input_string = input_string.replace(op, " @unary_op ")

  # Mengidentifikasi binary operator
  for op in _BINARY_OPERATORS:
    input_string = input_string.replace(op, " @binary_op ")

  # Memberikan spasi pada beberapa karakter
  for exp in _EXPANDS:
    input_string = input_string.replace(exp, " " + exp + " ")

  input_string = input_string.replace(_SPECIALS[0], " @assign_op ")
  
  # Menghilangkan newline
  input_string = input_string.replace("\n", " ")
  output_arr = input_string.split()

  # Validasi nama variabel menggunakan finite automata
  for i in range(len(output_arr)):
    str = output_arr[i]
    if str not in _KEYWORD and str not in _EXPANDS and str[0] != '@':
      state = finite_automata(str)
      if state == "q2":
        output_arr[i] = "@varname"
      elif state == "q3":
        output_arr[i] = "@value"
      else:
        output_arr[i] = "@invalid"

  for i in range(len(output_arr)):
    str = output_arr[i]
    if str == "@binary_op":
      output_arr[i] = "+"
    elif str == "@assign_op":
      output_arr[i] = "="

  return output_arr
