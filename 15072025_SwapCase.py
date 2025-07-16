def swap_case(s):
    s_list = list(s)
    #print(s_list)
    for i in range(len(s)):
        #print(s_list[i])
        if s_list[i].isupper():
            s_list[i] = s_list[i].lower()
        else:
            s_list[i] = s_list[i].upper()
    #print(s_list)
    return "".join(s_list)

# swaped_string = ""
#     for i in s:
#         if i.isupper():
#             swaped_string += i.lower()
#         else:
#             swaped_string += i.upper()
#     print(swaped_string)
#     return swaped_string

if __name__ == '__main__':
    a = swap_case("tesT")
    print(a)