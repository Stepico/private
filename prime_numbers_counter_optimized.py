class Solution:
    def countPrimes(self, n: int) -> int:
        cnt = 0

        for i in range(2, n):
            tmp = 0

            for j in range(2, i + 1):
                if i % j == 0:
                    tmp += 1

                if tmp >= 2:
                    break
            else:
                cnt += 1

        return cnt

    def countPrimes2(self, n: int) -> int:
        if n < 2:
            return 0

        # Create a boolean array to track prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        # Apply the Sieve of Eratosthenes algorithm
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as non-prime
                for j in range(i * i, n, i):
                    is_prime[j] = False

        # Count the number of prime numbers
        return sum(is_prime)


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes2(499979))


