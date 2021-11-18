"""
A - person ill
B - test is positive
C - false positive
P(A|B) = ?

P(A) = 0.1%
P(C) = 1%
P(B) = (1 - P(C)) * P(A) + P(C) * (1 - P(A))
P(B|A) - chance of test being positive if the person is ill
P(B|A) = (1 - P(C))

P(A|B) = P(A) * (1 - P(C)) / ( (1 - P(C)) * P(A) + P(C) * (1 - P(A)) )
"""

Pa = 0.1 / 100
Pc = 1 / 100
Pb = (1 - Pc) * Pa + Pc * (1 - Pa)
Pa_b = Pa * (1 - Pc) / ((1 - Pc) * Pa + Pc * (1 - Pa))
print(Pa_b * 100)  # 9.01639344262295
