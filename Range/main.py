# from itertools import groupby
# def ranges(lst):
#     pos = (j-i for i,j  in enumerate(lst))
#     t = 0
#     for i, els in groupby(pos):
#         l = len(list(els))
#         el = lst[t]
#         t+= 1
#         yield range(el,el+1)
#
#
# lst = list(range(1,100))
# print(list(ranges(lst)))


lst = list(range(1,20,2))
print(lst)