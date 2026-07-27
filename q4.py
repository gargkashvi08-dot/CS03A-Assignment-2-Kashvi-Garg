# /*****************************************************/
# /* CS03A - Summer 2026
# /* Assignment 2 - Question 4
# /* Student Name: Kashvi Garg
# /* SID: 20744788
# /*****************************************************/

def run():
    name=input('What is youre name? ')
    desc=input('Describe yourself. ')
    html='<html>\n<head>\n</head>\n<body>\n<center>\n<h1>'+name+'</h1>\n</center>\n<hr />\n'+desc+'\n</body>\n</html>'
    f=open('webpage.html','w')
    f.write(html)
    f.close()
    print('Webpage created: webpage.html')

if __name__=='__main__':
    run()
