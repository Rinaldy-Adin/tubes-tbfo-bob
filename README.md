# Tugas Besar Teori Bahasa Formal dan Otomata
Javascript Linter

## Anggota Kelompok:
- Rinaldy Adin 13521134
- Enrique Alifio Ditya 13521142
- Rava Maulana Azzikri 13521149

## Daftar Isi
* [Penjelasan Ringkas Program](#penjelasan-ringkas-program)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Struktur Folder](#struktur-folder)

## Penjelasan Ringkas Program
Dalam tugas besar ini, dilakukan pengimplementasian Teori Bahasa Formal dari *Context-free Grammar* dan *Finite Automata* dalam pembuatan program parser untuk bahasa pemrograman Javascript.
Parsing dilakukan menggunakan metode CYK (Cocke, Younger, Kasami) dengan mengubah terlebih dahulu grammar menjadi bentuk *Chomsky Normal Form* (CNF)

## Cara Menjalankan Program
1. Clone repository
    ```bash
    $ git clone https://github.com/Rinaldy-Adin/tubes-tbfo-bob.git
    ```
2. Masuk ke dalam folder project
    ```bash
    $ cd tubes-tbfo-bob
    ```
3. Jalankan program
    ```bash
    $ python src/main.py
    ```
## Struktur Folder
```
tubes-tbfo-bob
├── config
│   └── CFG.txt
├── out.txt
├── src
│   ├── CYK.py
│   ├── cfg_to_cnf.py
│   ├── finite_automata.py
│   ├── input_converter.py
│   ├── main.py
│   ├── testing.py
│   └── util.py
└── test
    ├── test_const_acc.js
    ├── test_const_rej.js
    ├── test_for_acc.js
    ├── test_for_rej.js
    ├── test_func_acc.js
    ├── test_func_rej.js
    ├── test_if_acc.js
    ├── test_if_rej.js
    ├── test_switch_acc.js
    ├── test_switch_rej.js
    ├── test_try_acc.js
    ├── test_try_rej.js
    ├── test_while_acc.js
    └── test_while_rej.js

```

## Made with
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
