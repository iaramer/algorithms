"""
Time limit	7 seconds
Memory limit	512Mb
Input	standard input or input.txt
Output	standard output or output.txt
After graduating from MIPT you've decided to apply your knowledge in AI to Physics. You've become a world-wide famous
physicist due to your deep knowledge of AI which you get on MSAI program. And now you are working on an innovational
quantum process research: sigma-trimpazation*. Your research is definitely going to change the world!

Your experiment is in progress. Quantum sensors are installed and send you data permanently. You've found a regularity
in this data. And now you are going to analyse it using python. What you need – is to get this data in sorted order.

Your process is initialized with three parameters: 0 ≤ N ≤ 107, 0 < M ≤ 104, 0 < q0 < 231. The process is the following:
your data sequence x is generated from quantum data sequence q. You are given q0 value and next items are generated
using the following rule** (this process is already implemented for you):
q_i = (q_{i-1} * 7^5) mod (2^31 - 1)

The data you need to analyze is calculated from quantum data: xi = (qi  mod  M) - M//2
Let's denote sorted data sequence as xs = sorted(x). You need to calculate the following value:
y = sum(i*x_spi-1])

You've tried to use built-it python sorting algorithm but it takes too much time
(your code is here: https://bit.ly/3vSlLpZ). You need to implement something faster.
Try to optimize it somehow. No time to obtain TL verdict! Research must go on!
"""


from time import time

estimate_execution_time = True

quantum_a = 7 ** 5
quantum_m = 2 ** 31 - 1


def analyze_trimpazation_original(n, m, q0):
    m_div2 = m // 2
    q = q0

    time11 = time()
    x = []
    for i in range(n):
        x_i = q % m - m_div2
        x.append(x_i)
        q = ((q * quantum_a) % quantum_m)
    print(time() - time11)

    time12 = time()
    x.sort()
    print(time() - time12)

    time13 = time()
    res = 0
    for i, v in enumerate(x):
        res += (i + 1) * v
    print(time() - time13)

    return res


def analyze_trimpazation(n, m, q0):
    m_div2 = m // 2
    q = q0

    time11 = time()
    x = []
    for i in range(n):
        x_i = q % m - m_div2
        x.append(x_i)
        q = ((q * quantum_a) % quantum_m)
    print(time() - time11)

    time12 = time()
    minx = - m_div2
    M = m
    a = [0] * M
    for v in x:
        a[v - minx] += 1
    print(time() - time12)

    time13 = time()
    res = 0
    asum_prev = 1
    for i, x_i in enumerate(a):  # i - element, x_i - repetitions
        asum = (2 * asum_prev + x_i - 1) * x_i
        res += (i + minx) * asum
        asum_prev += x_i
    print(time() - time13)
    return res // 2


if __name__ == '__main__':
    N, M, q0 = 10000000, 10000, 1
    # N, M, q0 = map(int, input().split())
    t = time()
    ans = analyze_trimpazation(N, M, q0)
    print(f'{ans} == 83287854395709985? Answer: {ans == 83287854395709985}')
    if estimate_execution_time:
        print(f'Execution time = {time() - t:.8f} seconds')
