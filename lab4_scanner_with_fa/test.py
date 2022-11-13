from scanner import Scanner

scanner = Scanner()

# pif, st, output_msg = scanner.scan_program("./programs/p1.txt")
# assert output_msg == "LEXICALLY CORRECT"
# # assert st.get_size() == 5
#
# print(output_msg)
# print()
#
# print("Symbol Table:")
# print(st)
# print()
#
# print("Program Internal Form:")
# for pif_elem in pif:
#     print(pif_elem)




pif, st, output_msg = scanner.scan_program("./programs/p2.txt")
assert output_msg == "LEXICALLY CORRECT"
# assert st.get_size() == 10

print(output_msg)
print()

print("Symbol Table:")
print(st)
print()

print("Program Internal Form:")
for pif_elem in pif:
    print(pif_elem)




# pif, st, output_msg = scanner.scan_program("./programs/p3.txt")
# assert output_msg == "LEXICALLY CORRECT"
# # assert st.get_size() == 7
#
# print(output_msg)
# print()
#
# print("Symbol Table:")
# print(st)
# print()
#
# print("Program Internal Form:")
# for pif_elem in pif:
#     print(pif_elem)



# _, st, output_msg = scanner.scan_program("./programs/p1err.txt")
