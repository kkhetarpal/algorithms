# def merge(B,C):
#     i, j = 0, 0
#     splits = 0
#     result = []
#     while i< len(B) and j< len(C):
#         if (B[i] < C[j]):
#             result.append(B[i])
#             i += 1
#         else:
#             result.append(C[j])
#             splits = splits + len(B[i:])
#             j += 1
#     result.extend(B[i:])
#     result.extend(C[j:])
#     #print result, splits
#     return result, splits

# def mergeandcount(A):
#     n = len(A)
#     if n < 2 : return A,0
#     B,splits1 = mergeandcount(A[:n/2])
#     C,splits2 = mergeandcount(A[n/2:])
#     sorted, splits3 = merge(B,C)
#     return sorted,(splits1+splits2+splits3)



P = [[1,2],[3,4],[7,8],[0,7],[0,4],[4,7]]
Px = []
Py = []
i = 0
while i < len(P):
    #print P[i]
    Px.append(P[i][0])
    Py.append(P[i][1])
    i += 1
print Px
print Py




