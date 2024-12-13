import math
string = "LVHUGlYJFLKCBROKHUCRUVJWKHLUKTHUCUBKZUBFLUXLKELUZLKDNRVENBWJLUKJWJDKLUXKBGLYJUBKZUBFLUXKEHUKBEHYJHUDFJWDFELVENLXEKOFJWBUXLEHYJHIWBMLNHKJHUDFJWDHUCIBDDLOGJOJGLJHOBRKCLQQJWJUKCJXWJJDBQVJWKHLUKTHOBRKCLQQJWJUKKELUXDORKLNUBKHODBGRKFGTDRWJBQHUTKELUXKEJWJHWJ".upper()
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index = {letter: caps.index(letter) for letter in caps}
rev_index = {caps.index(letter): letter for letter in caps}
print(index)


print([index[letter] for letter in string])
for b in range(26):
    for a in range(26):
        if math.gcd(a,26) == 1:
            print("a=",a,"b=",b,":")
            print(''.join(rev_index[(a*index[letter]+b) % 26] for letter in string))