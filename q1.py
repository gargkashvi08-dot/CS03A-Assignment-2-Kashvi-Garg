# /*****************************************************/
# /* CS03A - Summer 2026
# /* Assignment 2 - Question 1
# /* Student Name: Kashvi Garg
# /* SID: 20744788
# /*****************************************************/

def falling_distance(t):
    g=9.8
    d=0.5*g*t**2
    return d

def run():
    for t in range(1,11):
        print(falling_distance(t))

if __name__=='__main__':
    run()
