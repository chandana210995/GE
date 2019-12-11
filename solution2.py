with open("input.txt") as f:
    lines = f.read()
    for letters in lines:
        if letters.isalpha():
            if ord(letters)!=120 and ord(letters)!=121 and ord(letters)!=122 and ord(letters)!=88 and ord(letters)!=89 and ord(letters)!=90 :
                print(chr(ord(letters)+3), end="")
            else:
                print(chr(ord(letters)-23),end="")
        elif ord(letters)==32:
            print(" ",end="")
        else:
            print("")
