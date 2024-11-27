import string


def find_majority_element(lst):
    lst.sort()
    return lst[len(lst) // 2]

lst = [4, 2, 4, 4, 5, 4, 7, 4, 4, 5]
#output = find_majority_element(lst)
#print(output)

roman_dict = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
def convert_string_to_number(string):
    outcome = 0
    i = 0
    #letter = [char for char in string]
    if len(string) == 1:
        outcome = dict[string[0]]
    while i < len(string):
        if i + 1 < len(string) and roman_dict[string[i]] < roman_dict[string[i + 1]]:
            outcome += roman_dict[string[i + 1]] - roman_dict[string[i]]
            i += 2
        else:
            outcome += roman_dict[string[i]]
            i += 1
    return outcome


#string = "IL"
#print(convert_string_to_number(string))

def len_of_last_word(string):
    s = string.split()
    return len(s[-1])

#string = "    the  "
#print(len_of_last_word(string))
def len_of_last_word_with_out_split(s):
    i, length = len(s) - 1, 0
    while s[i] == " ":
        i -= 1
    while i >= 0 and s[i] != " ":
        length += 1
        i -= 1
    return length


string = "   gkjg ldk the moon  "
print(len_of_last_word_with_out_split(string))


def reverse_letters_in_words(s):
    # נפצל את המחרוזת למילים תוך הסרת רווחים מיותרים בתחילת ובסוף
    words = s.strip().split()

    # נהפוך את האותיות בכל מילה
    reversed_words = [word[::-1] for word in words]

    # נחבר את המילים מחדש עם רווח אחד בין כל מילה
    return " ".join(reversed_words)

s = "  Hello   world!  "
print(reverse_letters_in_words(s))  # הפלט: "olleH !dlrow"

def func(s):
    reverse_s = s[::-1]
    if len(reverse_s) == 1:
        return reverse_s
    else:
        first, last = len(s) - 2, len(s) - 1
        while first >= 0 and last == " ":
            first -= 1
            last -= 1
        while first >= 0 and last != " " and first != " ":
            first -= 1

            i -= 1

