"""def is_palindrome(string):
    string = string.lower()
    new_string = ""
    for c in string:
        if 97 <= ord(c) <= 122 or 48 <= ord(c) <= 57:
            new_string += c
    return new_string == new_string[::-1]

a = is_palindrome("Ae44Ea")

def is_palindrome2(string): #memory complexity O(1)
    string = string.lower()
    left, right = 0, len(string)-1
    while right > left:
        while not string[right].isalnum():
            right -= 1
        while not string[left].isalnum():
            left += 1
        if string[right] != string[left]:
            return False
        else:
            right -= 1
            left += 1
    return True

a = is_palindrome2("A#e74Ea") """

def ransom_note(ransomNote, magazine):
    magazine = magazine.lower()
    ransomNote = ransomNote.lower()
    for i in ransomNote:
        if i not in magazine:
            return False
        else:
            idx = magazine.index(i)
            magazine = magazine[:idx] + magazine[idx+1:]
    return True

a = ransom_note("ag a", "agb a")

"""def summery_ranges(nums):
    new_arr = []
    i = 1
    for number in nums:
        if number+1 != nums[i]:
            new_arr.append(number)
            #print(number)
        else:
            i += 1
    return print(new_arr)

nums = [0, 1, 2, 4, 5, 7]
range = summery_ranges(nums)"""