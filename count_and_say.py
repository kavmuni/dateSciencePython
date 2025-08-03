class count_and_say:
    def digts_and_freq(string1:str):
        if not string1:
            return -1

        lv_main_list = []
        lv_count = 0
        lv_string = string1[0]

        for i in string1:
            lv_list = []
            #lv_count += 1
            print(i, lv_count, lv_string)
            if lv_string == i:
                lv_count += 1
            else:
                lv_count = 1

            lv_list = [lv_count, int(i)]
            print(i, lv_count, lv_string, lv_list)
            lv_main_list.append(lv_list)
            lv_string = i

        print(lv_main_list)
        return lv_main_list

solution = count_and_say
solution.digts_and_freq("11223")
