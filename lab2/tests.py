from symbol_table import SymbolTable

st = SymbolTable()
st.add_elem("test")
assert st.find_element_position("test") == (6, 0)

st.add_elem("a")
st.add_elem("b")
st.add_elem("c")
assert st.find_element_position("a") == (12, 0)
assert st.find_element_position("b") == (13, 0)
assert st.find_element_position("c") == (14, 0)

st.add_elem(-2)
st.add_elem(0)
st.add_elem(1)

assert st.find_element_position(-2) == (10, 0)
assert st.find_element_position(0) == (14, 1)    # "0" % m has the same ascii sum as "c", so we have a collision
assert st.find_element_position(1) == (15, 0)

st.add_elem("print")
st.add_elem("nice_message")

assert st.find_element_position("print") == (13, 1)    # same ascii sum as "b"
assert st.find_element_position("nice_message") == (10, 1)   # same ascii sum as "-2"
