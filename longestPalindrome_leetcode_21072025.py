import datetime


class Solution:
    def __init__(self, s: str):
        self.string_ = s

    def longestPalindrome(self) -> str:
        # First form different substrings from the given big string
        # then check if the substrings are Palindrome or NOT
        # check length of each substring and return largest  value
        if len(self.string_) <= 1:
            return self.string_

        s_dict = {}
        # for i in range(len(self.string_)):
        #     #print(self.string_[i-1:len(self.string_)+i:2])
        #     #print(self.string_[i:len(self.string_) - i])
        #     print(i, self.string_[i:len(self.string_) - i], "".join(reversed(self.string_[i:len(self.string_) - i])))
        #     if self.string_[i:len(self.string_) - i] == "".join(reversed(self.string_[i:len(self.string_) - i])):
        #         s_dict[len(self.string_[i:len(self.string_) - i])] = self.string_[i:len(self.string_) - i]
        print((datetime.datetime.now()))
        for i in range(len(self.string_)):
           for j in range(i+1, len(self.string_)+1):
             if self.string_[i:j] == "".join(reversed(self.string_[i:j])):
                 s_dict[len(self.string_[i:j])] = self.string_[i:j]

        print(s_dict)
        print(s_dict[max(s_dict.keys())])
        print((datetime.datetime.now()))

test_solution = Solution("rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip")
test_solution.longestPalindrome()