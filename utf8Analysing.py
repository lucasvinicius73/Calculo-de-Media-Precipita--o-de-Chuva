import sys

with open ("DataSet/data.csv","r",encoding="utf-8") as f:
    for i in f:
            for c in i:
                 if(ord(c)<128):
                     print(c,end=",")