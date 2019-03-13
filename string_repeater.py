"""
Answer to a question from some website with alghoritms
Might be from google academics or sth
Replaces <n>[<text>] with text repeated n times
3[abc] -> abcabcabc
Supports nested arguments
"""

def looper(times,string):
    return int(times)*string

def replace(text,start,end,replacement):
    return text[:start] + replacement + text[end:]

def replace_deepest(text):
    # find first closing bracket
    pos2 = text.find(']')
    # find matching opening bracket
    for x in range(pos2,0,-1):
        if text[x] == '[':
            pos1 = x
            break
    # find matching number of repetitions
    num = ""
    lindex = pos1-1
    while lindex>=0:
        if text[lindex].isdigit():
            num = text[lindex] + num
        else:
            break
        lindex -= 1
    # replace number+bracket with correct version
    text = replace(text,lindex+1,pos2+1,looper(num,text[pos1+1:pos2]))
    return text

def full_replacement(text):
    res = text[:]
    while res.find(']')!=-1:
        res = replace_deepest(res)
    return res

ts1 = "3[abc]4[ab]c"
ts2 = "10[a]"
ts3 = "2[3[a]b]"


print(full_replacement(ts1))
