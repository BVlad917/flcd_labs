from scanner import Scanner

scanner = Scanner()

pif, st, output_msg = scanner.scan_program("./programs/p1.txt")
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




# pif, st, output_msg = scanner.scan_program("./programs/p2.txt")
# assert output_msg == "LEXICALLY CORRECT"
# # assert st.get_size() == 10
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

# def __get_strings_outside_indexes(string, indexes):
#     if not len(indexes): return []
#     strings = [string[:indexes[0][0]]]
#     start = indexes[0][1]
#     for index_pair in indexes[1:]:
#         end = index_pair[0]
#         strings.append(string[start + 1: end])
#         start = index_pair[1]
#     strings.append(string[indexes[-1][1] + 1:])
#     return [s for s in strings if len(s) > 0]
#
# def __get_strings_between_indexes(string, index_pairs):
#     return [string[start: end + 1] for start, end in index_pairs]
#
# def __find_indexes_of_char(string, char):
#     return [idx for idx, ltr in enumerate(string) if ltr == char]
#
# def __group_quotes(line, quote_type):
#     quote_indexes = __find_indexes_of_char(line, quote_type)
#     num_quotes = len(quote_indexes)
#     if num_quotes % 2 == 1:
#         quote_description = "double" if quote_type == '"' else "single"
#         raise KeyError(f"Missing {quote_description} quote in the following line: {line}")
#     return [(quote_indexes[i], quote_indexes[j])
#             for i, j in zip(range(0, num_quotes, 2), range(1, num_quotes, 2))]
#
#
# def __extract_strings_and_chars(line):
#     grouped_string_delim = __group_quotes(line, '"')
#     grouped_char_delim = __group_quotes(line, "'")
#     all_delimiters = sorted(grouped_string_delim + grouped_char_delim, key=lambda x: x[0])
#     new_delimiters = []
#     for delim1, delim2 in zip(all_delimiters[:-1], all_delimiters[1:]):
#         new_delimiters.append((delim1[1] + 1, delim2[0] - 1))
#     all_delimiters = sorted(all_delimiters + new_delimiters, key=lambda x: x[0])
#     all_delimiters.insert(0, (0, all_delimiters[0][0] - 1))
#     all_delimiters.append((all_delimiters[-1][1] + 1, len(line) - 1))
#
#     string_constants = __get_strings_between_indexes(line, all_delimiters)
#     # char_constants = __get_strings_between_indexes(line, grouped_char_delim)
#     # non_string_or_char = __get_strings_outside_indexes(line, all_delimiters) if len(all_delimiters) else [line]
#     return string_constants#, char_constants, non_string_or_char
#
#
# __extract_strings_and_chars('write("Minimum is ")')