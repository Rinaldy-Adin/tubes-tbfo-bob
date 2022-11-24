_TRANSITIONS = {
    "q0": {
      "alphabet": "q2",
      "underscore": "q2",
      "number": "q1",
      "else": "q1"
    },
    "q1": {
      "alphabet": "q1",
      "underscore": "q1",
      "number": "q1",
      "else": "q1"
    },
    "q2": {
      "alphabet": "q2",
      "underscore": "q2",
      "number": "q2",
      "else": "q1"
    }
  }
_KEYWORD = ["break", "const", "case", "catch", "continue", "default", "delete", "else", "false", "finally", "for", "function", "if", "let", "null", "return", "switch", "throw", "try", "true", "var", "while"]

def finite_automata(input_str):
  """Finite automata untuk memvalidasi penamaan variabel"""
  # State awal
  state = "q0"

  # Membaca setiap karakter pada input string
  for char in input_str:
    curr_ascii = ord(char)
    if char == '_':
      curr_char = "underscore"
    elif 65 <= curr_ascii <= 90 or 97 <= curr_ascii <= 122:
      curr_char = "alphabet"
    elif 48 <= curr_ascii <= 57:
      curr_char = "number"
    else:
      curr_char = "else"

    # Melakukan transisi berdasarkan input  
    state = _TRANSITIONS[state][curr_char]

  # Menghasilkan true jika automata berada di final state (q2)
  return state == "q2"

