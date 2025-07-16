def minion_game(string):
    stuart=0
    kevin=0
    words_list=[]
    # to check upper case constraint
    if string.islower():
        print(f"{string} is NOT in upper case")
        return -1
    # since the string is in capital given the vowel list in capital
    vowels = ['A','E','I','O','U']
    for i in range(0,len(string)+1):
        # slicing word into different string and storing in list
        for j in range(i,len(string)+1):
            #print(i,j)
            words = string[i:j].strip()
            #print(words)
            if words != "":
                words_list.append(words)
    words_list.sort()
    #print(words_list)
    # form a dictionary with word as key and occurrence as values
    word_dict = {}
    word2 = ""
    word1_count = 1
    for i in words_list:
        word1 = i.strip()
        #print(word1, word2, word1_count)
        #print(type(word1), type(word2))
        if word1 == word2:
            word2 = word1
            word1_count += 1
        else:
            word2 = word1
            word1_count = 1
        word_dict[i] = word1_count
    #print(word_dict)
    for key, value in word_dict.items():
        #print(type(key), key[0])
        if vowels.__contains__(key[0]):
            kevin += value
        else:
            stuart += value
    #print(stuart, kevin)
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
    return 1
minion_game("NANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANANNANA")

# def minion_game(string):
#     w = string
#     k =0
#     s =0
#     for i in range(len(w)):
#         print(w[i])
#         if w[i] in ["A","E","I","O","U"]:
#             k += len(w)-i
#         else:
#             s+=len(w)-i
#     if k > s:
#         print("Kevin",k)
#     elif s>k :
#         print("Stuart",s)
#     else:
#         print("Draw")
#
# minion_game("BANANA")