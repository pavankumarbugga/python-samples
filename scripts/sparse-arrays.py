# https://www.hackerrank.com/challenges/sparse-arrays/problem?h_r=next-challenge&h_v=zen

from collections import Counter

def matchingStrings(strings, queries):
    # create a dictionary with count
    s = Counter(strings)
    print(s) 
    result = []
    for i in queries:
        result.append(s[i])
    print(result)

strings = ["ab","ab","abc"]
queries = ["ab","abc","bc"]
matchingStrings(strings,queries)