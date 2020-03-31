def string_compression(s: str) -> str:
    output = ""
    count = 1
    for i in range(len(s)):
        if i == 0:
            output += s[i]
        else:
            if s[i] != s[i - 1]:
                output += str(count)
                count = 1
                output += s[i]
            else:
                count += 1
    output += str(count)

    if len(output) < len(s):
        return output
    else:
        return s


print(string_compression("aaaaaaaassdcfeecdd"))
print(string_compression("aaassdcfeecdd"))
