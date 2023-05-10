
#plate calculator


#variables: 
# W is total weight
# X is weight without bar (45 pounds)
# Y is 45 pound plates
# Z is 25 pound plates
# C is 10 pound weights
# D is 5 pound plates
# F is 2.5 pound plates
# A is weight without 45s(A=X-(Y*90))
# B is weight without 25s
# E is weight without 10s
# G is weight without 5s

while True:
    print("What is the weight you would like to calculate")
    W= input("input weight here __") 
    X=int(W)-45
    Y=X//(90)
    print(str(Y) + " 45 Pound Plate per side")
    A=X-(Y*90)
    Z=A//50
    print(str(Z) + " 25 Pound Plates per side")
    B=A-(Z*50)
    C=B//20
    print(str(C) + " 10 Pound Plates per side")
    E=B-(C*20)
    D=E//10
    print(str(D) + " 5 Pound Plates per side")
    G=E-(D*10)
    F=G//5
    print(str(F) + " 2.5 Pound Plates per side")
    continue