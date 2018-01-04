#!/usr/bin/python
# -*- coding: utf-8 -*--

def wans(arg1, arg2, arg3):
    
    # set parameter
    row = arg1
    col = arg2
    nameWan = arg3  #"face" or "body"
    
    # load unicode emoji
    face = "\U0001f436"     # face only
    body = "\U0001F415"     # with body
    panda = "\U0001F43C"      # panda 
     
    # select emoji
    if nameWan == "face":
        wan = face
    elif nameWan == "body":
        wan = body
    elif nameWan == "panda":
        wan = panda
    else:
        print("select face or body", file=sys.stderr)

    #make listWan
    listWan = [[0 for column in range(0,col)] for row in range(0,row)]
    for i in range(0,row):
        for j in range(0,col):
            listWan[i][j] = wan
            # print
            if j==col-1:
                print(wan,end="\n")
            else:
                print(wan,end=" ")
    return listWan

# main
if __name__ == "__main__":
    row = 15
    col = 1
    name = "face"
    #name = "body"
    listWans = wans(row,col,name)
    print(listWans)
