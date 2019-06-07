n = int(input())
m = int(input())
diff_n = int(input())
diff_m = int(input())

prime_counter_n = 0
prime_counter_m = 0
max_n = n + diff_n
max_m = m + diff_m

for i in range(n, max_n+1):
    for k in range(m, max_m+1):
        for is_i_prime in range(1, i+1):
            if i % is_i_prime == 0:
                prime_counter_n += 1

        for is_k_prime in range(1, k+1):
            if k % is_k_prime == 0:
                prime_counter_m += 1

        if prime_counter_n == 2 and prime_counter_m == 2:
            print(f"{i}{k}")
        prime_counter_n = 0
        prime_counter_m = 0