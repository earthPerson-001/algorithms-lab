import itertools

from src.lab3.utils import list_scaler_multiply

def knapsack_0_1_bruteforce(profits, weights, max_capacity):
    length = len(profits)

    current_max_profit = 0

    selected_indices = [0 for _ in range(length)]

    lst = list(itertools.product([0, 1], repeat=len(profits)))

    for val in lst:
        current_selected = list(val)

        if sum(list_scaler_multiply(weights, current_selected)) <= max_capacity:
            current_profit = sum(list_scaler_multiply(profits, current_selected))

            if current_profit > current_max_profit:
                current_max_profit = current_profit
                selected_indices = current_selected
    
    return selected_indices

if __name__ == "__main__":
    profits = [10, 15, 20]
    weights = [100, 200, 300]
    max_capacity = 400

    ret = knapsack_0_1_bruteforce(profits, weights, max_capacity)
    print(ret)
