lst_str = ["aaa","aab","dac"]
i = 0
pre_match = []
for str_element in lst_str :
    for str_index in str_element :
    i = i + 1
    if i == 1:

        pre_match = str_element[0]
    if i!=1:
        if pre_match == str_element[0]:
            continue

        else:
            pre_match = "null"

print pre_match

