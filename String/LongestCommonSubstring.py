from difflib import SequenceMatcher

#  longest common substring

str1 = "zxabcdezy"
str2 = "yzabcdezx"

seqMatch = SequenceMatcher(None, str1, str2)

match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))

if match.size != 0:
    print(str1[match.a: match.a + match.size])
else:
    print('No longest common sub-string found')

