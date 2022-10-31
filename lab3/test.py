from scanner import Scanner

scanner = Scanner()

_, st, output_msg = scanner.scan_program("./programs/p1.txt")
assert output_msg == "LEXICALLY CORRECT"
assert st.get_size() == 5
# print("Symbol Table:")
# print(st)

# _, st, output_msg = scanner.scan_program("./programs/p2.txt")
# assert output_msg == "LEXICALLY CORRECT"
# assert st.get_size() == 13
# # print("Symbol Table:")
# # print(st)
#
# _, st, output_msg = scanner.scan_program("./programs/p3.txt")
# assert output_msg == "LEXICALLY CORRECT"
# assert st.get_size() == 17
# # print("Symbol Table:")
# # print(st)
#
# _, st, output_msg = scanner.scan_program("./programs/p1err.txt")
# assert "Missing double quote" in output_msg
