# title
# st = "how are you"
# print(st.title())

# strip the start and end occrance of target
# st = "ppp how are youpppp"
# print(st.strip("p"))


# reverse a string
# st = "akash"
# print(st[::-1])


# repeat
# import itertools
# print(list(itertools.repeat("akash",5)))


# longest common subsequece
# from difflib import SequenceMatcher
# ab = "abcdefght"
# bb = "abcdklete"
# seqMatch = SequenceMatcher(None, ab, bb)
# mtch = seqMatch.find_longest_match(0, len(ab), 0, len(bb))
# if mtch.size !=0:
#     # print(mtch.a, mtch.a+mtch.size)
#     print(ab[mtch.a : mtch.a + mtch.size])



# join the list
# s = ['p', 'a', 'g', 'e']
# print("".join(s))


# is title?
# st = "Welcome In India"
# res = st.istitle()
# print(res)


# Is digits
# n = "1212"
# ans = n.isdigit()
# print(ans)


# slicing the string
# st= 'hii how are you man'
# slc = st[3:8]
# print(slc)


# count he occurance of a word in a line
# st = "welcome to geeks for geeks"
# cnt = st.count("geeks")
# print(cnt)