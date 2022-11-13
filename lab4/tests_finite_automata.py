from finite_automata import FiniteAutomata

# file_path = "./fa.in"
# fa = FiniteAutomata(file_path)
# print(fa.is_sequence_accepted(""))

from string import ascii_lowercase, ascii_uppercase
for c in '0123456789' + ascii_lowercase + ascii_uppercase:
    print(f"(qf, {c}, qf)", end=' ')
