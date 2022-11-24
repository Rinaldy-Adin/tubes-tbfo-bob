_ALPHANUM = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 58)] + ["_"]
_OPERATORS = [">>>=", "===", "!==", "<<=", ">>=", "**=", "&&=", "||=", "??=", ">>>","+=", "-=", "*=", "/=", "%=", "&=", "^=", "|=", "==", "!=", ">=", "<=", "++", "--", "**", "<<", ">>", "&&", "||", "??", "%", "+", "-", "*", "/" "=", ">", "<", "&", "|", "^", "~"]
_EXPANDS = ["(", ")", "{", "}", "[", "]", "?", ":", ",", ";"]


def convert_input(input_string):
  """Fungsi untuk mengubah string node js menjadi sebuah array"""
  # Mengidentifikasi semua operator
  for op in _OPERATORS:
    input_string = input_string.replace(op, " @operator ")

  # Memberikan spasi pada beberapa karakter
  for exp in _EXPANDS:
    input_string = input_string.replace(exp, " " + exp + " ")

test_str = "if (x == 0) {\n return 0;\n} else if (x + 4 == 1) {\n if (true)"