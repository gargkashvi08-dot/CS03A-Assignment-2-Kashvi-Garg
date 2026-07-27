# /*****************************************************/
# /* CS03A - Summer 2026
# /* Assignment 2 - Question 2
# /* Student Name: Kashvi Garg
# /* SID: 20744788
# /*****************************************************/

def show_prime(n):
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
            break
    if prime:
        print(str(n)+' is a prime number')
    else:
        print(str(n)+' isnt a prime number')

def run():
    n=int(input('Enter an integer greater than 1: '))
    nums=list(range(2,n+1))
    for x in nums:
        show_prime(x)

if __name__=='__main__':
    run()
