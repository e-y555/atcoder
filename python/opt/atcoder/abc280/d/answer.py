K = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

prime_list = prime_factorize(K)
prime_list.sort()
fact_list=[]
iteration_count=0
while 1:
    if prime_list == []:
        break
    iteration_count+=1
    p = prime_list.pop(0)
    q = 1
    p2 = p
    while 1:
        if p2 not in fact_list:
            fact_list.append(p2)
            break
        p2 += p
        q += 1
    for pw in (prime_list[:]):
        if pw > q:
            break
        if q % pw == 0:
            prime_list.remove(pw)
            q /= pw
print(max(fact_list))