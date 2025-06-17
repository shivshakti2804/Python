String = input("Enter a String to reverse: ")
def Stringreverse(String):
    Reversed_String = ""
    for i in String:
        if i == "a":
            break
            #continue ---Use continue to skip the character a and continue to reverse rest
        Reversed_String = i + Reversed_String
    return Reversed_String

print("The reversed value is", Stringreverse(String))
