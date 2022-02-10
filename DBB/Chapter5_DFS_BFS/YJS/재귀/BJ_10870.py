'''
fibo_0 = 0
fibo_1 = 1
fibo_n = fibo_n_2 + fibo_n_3
       = fibo_n_4 + fibo_n_3 + fibo_n_5 + fibo_n_4
'''
def rec_fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return rec_fibo(num-2)+rec_fibo(num-1)
    
n = int(input())
print(rec_fibo(n))
    