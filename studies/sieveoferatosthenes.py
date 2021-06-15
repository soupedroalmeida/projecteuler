def sieve_Eratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while(p * p <= n): 
        if (prime[p] == True):
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
    prime[0] = None
    prime[1] = None
    return prime