def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not 1 < len(s) < 7:
        return False

    letters = 0
    numbers = 0
    type = True  # True = letters, False = nums
    for a in s:
        if not a.isalnum():
            return False
        if a.isalpha():
            if type:
                letters += 1
            else:
                return False
        else:
            if numbers == 0 and a == '0':
                return False
            numbers += 1
            type = False

    if letters < 2:
        return False




    return True
main()
