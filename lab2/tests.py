from symbol_table import SymbolTable

st = SymbolTable()
st.add_elem("test")    # length = 4
assert st.find_element_position("test") == 4

st.add_elem("a")
st.add_elem("b")
st.add_elem("c")
assert st.find_element_position("a") == 1
assert st.find_element_position("b") == 1
assert st.find_element_position("c") == 1

st.add_elem(-2)
st.add_elem(0)
st.add_elem(1)
assert st.find_element_position(-2) == 2
assert st.find_element_position(0) == 1
assert st.find_element_position(1) == 1

st.add_elem("print")
st.add_elem("nicemessage")
assert st.find_element_position("print") == 5
assert st.find_element_position("nicemessage") == 11
