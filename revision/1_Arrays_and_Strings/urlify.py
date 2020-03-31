def urlify(s: str) -> str:
    output = ""
    for c in s:
        if c == " ":
            output += "%20"
        else:
            output += c
    return output


print(urlify("asd asd fvd  asdnasjkdn     L"))
