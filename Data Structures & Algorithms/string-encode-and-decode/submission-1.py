class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for s in strs:
            encode_str += f"{len(s)}#{s}"

        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_str = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j+1
            end = start + length

            decode_str.append(s[start:end])
            i = end

        return decode_str

# encoder takes in string input so need encode = "" initialization
# but decoder needs to output a list so decode initialized as list
# length prefixing done to store the indiviual strings as length with 
# string itself. we use # as a way to differentiate b/w len and string
# then we use 2 points i and j to keep a track to get the string and len
# int(s[i:j]) is important and not just s[i] since len can be more than 
# 1 digit too so need i:j
