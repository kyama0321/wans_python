#!/usr/bin/python3
# -*- coding: utf-8 -*--
import sys


def wans(arg1, arg2, arg3):
    # set parameter
    row = arg1
    col = arg2
    name_wan = arg3  # "face" or "body"
    
    # load unicode emoji
    face = "\U0001f436"     # face only
    body = "\U0001F415"     # with body
    panda = "\U0001F43C"      # panda 
     
    # select emoji
    if name_wan == "face":
        wan = face
    elif name_wan == "body":
        wan = body
    elif name_wan == "panda":
        wan = panda
    else:
        print("select face or body", file=sys.stderr)

    # make listWan
    list_wan = [[0 for column in range(0, col)] for row in range(0, row)]
    for i in range(0, row):
        for j in range(0, col):
            list_wan[i][j] = wan
            # print
            if j == col-1:
                print(wan, end="\n")
            else:
                print(wan, end=" ")
    return list_wan


def main(args):
    row = args.row
    col = args.col
    name = args.name

    list_wans = wans(row, col, name)

    print(list_wans)


# main
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--row', default=5, type=int)
    parser.add_argument('-c', '--col', default=5, type=int)
    parser.add_argument('-n', '--name', default='face', type=str, choices=['face', 'body', 'panda'])

    opt = parser.parse_args()

    main(opt)
