from fa_ui import FaMenu
from finite_automata import FiniteAutomata

file_path = "./fa2.in"
fa = FiniteAutomata(file_path)
menu = FaMenu(fa)
menu.run_menu()
