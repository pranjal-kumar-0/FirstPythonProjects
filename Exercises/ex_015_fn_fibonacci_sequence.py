# Fibonacci Sequence Generator

def fibonacci(frequency):
    sequence = [0,1]
    for i in range(frequency-2):
        c_term = sequence[-2] + sequence [-1]
        sequence.append(c_term)
    return sequence
