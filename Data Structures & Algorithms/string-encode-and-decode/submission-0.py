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
