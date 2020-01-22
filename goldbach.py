prime_list = [2, 3, 5, 7, 11, 13]
wrong_answers = [False, True, True, False, True, False, True, False, False, False, True, False, True]
# initialized with six already-known primes
for i in range(0, 20_000):
    # length exceeds the range we will be checking, which is 0 to 10,000
    wrong_answers.append(False)


def find_prime(n):
    """Generates a table of prime numbers.
    Also sets wrong_answers to true at each the index of each prime(considering the 0th index to be 1).
    :param n: The desired number of primes """
    prime_count = len(prime_list)
    if prime_count >= n:
        return prime_list[n - 1]
    else:
        current_number = prime_list[prime_count - 1] + 2
        while prime_count < n:
            factor_found = False
            for i in prime_list:
                if current_number % i == 0:
                    factor_found = True
                    break
                if i >= pow(current_number, .5):
                    break
            if not factor_found:
                prime_list.append(current_number)
                wrong_answers[current_number - 1] = True
                prime_count += 1
            current_number += 2
            factor_found = False
    return prime_list[n - 1]


def generate_goldbach(n):
    """Generates all possible goldbach numbers up to a given number."""
    for i in range(1, int(.5 * (pow(n, .5)))):
        two_square = 2 * pow(i, 2)
        for j in prime_list:
            wrong_answers[two_square + j - 1] = True


def check_answers(small, big):
    """Checks wrong_answers for any odd, non-prime numbers that weren't generated by the goldbach function.
    Stops when it gets to the smallest possible solution."""
    winner = 0
    for i in range(small, big):
        if not (wrong_answers[2 * i - 2]):
            winner = 2 * i - 1
            break
    return winner


find_prime(1229)
print(prime_list)
generate_goldbach(10001)
print(wrong_answers)
print(check_answers(3, 10000))
