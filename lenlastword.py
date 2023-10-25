S = 'Hello world'
def lengthOfLastWord(S):
        count = 0
        length_last = 0
        for i in S:
            if i == ' ':
                count = 0
            else:
                count = count + 1
                length_last = count 
        return length_last
print(lengthOfLastWord(S))
