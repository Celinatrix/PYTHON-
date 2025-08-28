N = int(input("Nhập số N: "))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(2, N):
    if is_prime(i):
        primes.append(i)
prime_dict = {}
for idx, val in enumerate(primes, start=1):
    prime_dict[idx] = val
print("Dictionary chứa số nguyên tố nhỏ hơn", N, ":")
print(prime_dict)
