class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        encodedStr =""
        for s in strs:
            for c in s:
                encodedStr += str(ord(c))
                # ':' signifies end of character
                encodedStr += ':'
            # ';' signifies end of string
            encodedStr += ';'
        return encodedStr

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        decodedStrs = []
        dString = ""
        buff = ""
        for c in str:
            if c != ':' and c != ';':
                buff += c
            elif c == ':':
                dString += chr(int(buff))
                buff = ""
            else:
                decodedStrs.append(dString)
                dString = ""
        return decodedStrs