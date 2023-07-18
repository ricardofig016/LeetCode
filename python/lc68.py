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
        if curr_line:
            lines.append(curr_line[:-1])

        for i in range(len(lines)):
            missing = maxWidth - len(lines[i])
            spaces = 0
            for ch in lines[i]:
                if ch == " ":
                    spaces += 1
            if spaces == 0 or i == len(lines) - 1:
                lines[i] += " " * missing
            else:
                increment = missing // spaces
                rest = missing % spaces
                j = 0
                space_counter = 0
                while j < len(lines[i]):
                    if lines[i][j] == " ":
                        space_counter += 1
                        lines[i] = lines[i][:j] + " " * increment + lines[i][j:]
                        if space_counter <= rest:
                            lines[i] = lines[i][:j] + " " + lines[i][j:]
                            j += 1
                        j += increment
                    j += 1

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
words4 = ["Here", "is", "an", "example", "of", "text", "justification."]
maxWidth4 = 14
s = Solution()
print(s.fullJustify(words1, maxWidth1))
print(s.fullJustify(words2, maxWidth2))
print(s.fullJustify(words3, maxWidth3))
print(s.fullJustify(words4, maxWidth4))
