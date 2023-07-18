class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        curr_line = ""
        for word in words:
            if len(word) <= maxWidth - len(curr_line):
                curr_line += word + " "
            elif len(word) == maxWidth:
                lines.append(curr_line[:-1])
                lines.append(word)
                curr_line = ""
            else:
                lines.append(curr_line[:-1])
                curr_line = word + " "
        lines.append(curr_line[:-1])
        return lines


words1 = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth1 = 16
words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth2 = 16
words3 = [
    "Science",
    "is",
    "what",
    "we",
    "understand",
    "well",
    "enough",
    "to",
    "explain",
    "to",
    "a",
    "computer.",
    "Art",
    "is",
    "everything",
    "else",
    "we",
    "do",
]
maxWidth3 = 20
s = Solution()
print(s.fullJustify(words1, maxWidth1))
print(s.fullJustify(words2, maxWidth2))
print(s.fullJustify(words3, maxWidth3))
