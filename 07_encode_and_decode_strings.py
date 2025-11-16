"""
Encode and Decode Strings
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
    Input: ["neet","code","love","you"]
    Output:["neet","code","love","you"]

Example 2:
    Input: ["we","say",":","yes"]
    Output: ["we","say",":","yes"]
    
Constraints:
    0 <= strs.length < 100
    0 <= strs[i].length < 200
    strs[i] contains only UTF-8 characters.
"""

from typing import List
import time

class MySolution:
    def encode(self, strs: List[str]) -> str:
        msg = ""
        for word in strs:
            header = len(word)
            msg = msg + f"{header}#{word}"
            
        return msg

    def decode(self, s: str) -> List[str]:
        msg = s
        words = []
        while msg != "":
            idx = msg.index("#")
            leng = int(msg[:idx])
            tail = msg[idx+1:]
            word = tail[:leng]
            msg = tail[leng:]
            
            words.append(word)
            
        return words

if __name__ == "__main__":
    mysol = MySolution()
    
    print("-" * 50)
    start_time = time.time()
    output = mysol.encode(["neet","code","love","you"])
    print(output)
    output = mysol.decode(output)
    print(output)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time:.6f} seconds")