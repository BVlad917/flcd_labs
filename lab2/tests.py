from symbol_table import SymbolTable

st = SymbolTable()

# add an element in the symbol table and check that it was added on the correct position according to
# the chosen hash function
st.add_elem("test")
assert st.find_symbol_position("test") == (6, 0)

# add a few more elements and check their positions, none have collisions
st.add_elem("a")
st.add_elem("b")
st.add_elem("c")
assert st.find_symbol_position("a") == (12, 0)
assert st.find_symbol_position("b") == (13, 0)
assert st.find_symbol_position("c") == (14, 0)

# add some more elements, one of them will have a collision with a previously added element
st.add_elem(-2)
st.add_elem(0)
st.add_elem(1)

assert st.find_symbol_position(-2) == (10, 0)
assert st.find_symbol_position(0) == (14, 1)    # "0" % m has the same ascii sum as "c", so we have a collision
assert st.find_symbol_position(1) == (15, 0)

# add string elements as well
st.add_elem("print")
st.add_elem("nice_message")

assert st.find_symbol_position("print") == (13, 1)    # same ascii sum as "b"
assert st.find_symbol_position("nice_message") == (10, 1)   # same ascii sum as "-2"

# search for elements which were not added in the symbol table and check that the output is right
assert st.find_symbol_position("non-existing-string")[1] == -1

# check that trying to add an existing element raises an exception
try:
    st.add_elem(0)
    assert False
except ValueError:
    assert True
