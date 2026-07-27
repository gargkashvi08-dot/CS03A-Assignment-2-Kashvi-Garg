# /*****************************************************/
# /* CS03A - Summer 2026
# /* Assignment 2 - Question 3
# /* Student Name: Kashvi Garg
# /* SID: 20744788
# /*****************************************************/

def capitalize_sentences(text):
    parts=[]
    cur=''
    for c in text:
        cur+=c
        if c in '.!?':
            parts.append(cur)
            cur=''
    if cur.strip():
        parts.append(cur)
    result=[]
    for p in parts:
        p=p.strip()
        if p=='':
            continue
        i=0
        while i<len(p) and not p[i].isalpha():
            i+=1
        p=p[:i]+p[i:i+1].upper()+p[i+1:]
        result.append(p)
    return ' '.join(result)

def run():
    text=input('Enter a string: ')
    print(capitalize_sentences(text))

if __name__=='__main__':
    run()
