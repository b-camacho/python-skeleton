# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish

print("test")

def question01(portfolios):
    print(portfolios)
    # modify and then return the variable below
    answer = brute(portfolios)
    return answer


def brute(portfolios):
    cur_max = 0
    for i in range(0, len(portfolios)):
        for j in range(i, len(portfolios)):
            cur_max = max(cur_max, portfolios[i] ^ portfolios[j])

    return cur_max


