import itertools

from src.lab3.utils import list_scaler_multiply

def fill_remaining_with_best_weights(
    profits, weights, max_capacity, current_selected: list
):
    unfilled_weight = max_capacity - sum(
        list_scaler_multiply(current_selected, weights)
    )

    if unfilled_weight < 1:
        return current_selected

    max_profit = sum(list_scaler_multiply(current_selected, profits))
    optimal_selection = current_selected.copy()
    for i, _ in enumerate(profits):
        if not current_selected[i]:  # if the weights has not been selected
            frac_current_selection: list[float] = current_selected.copy()
            frac_current_selection[i] = min(float(unfilled_weight) / float(weights[i]), 1.0) # don't let it exceed 1

            current_profit = sum(list_scaler_multiply(frac_current_selection, profits))

            if current_profit > max_profit:
                max_profit = current_profit
                optimal_selection = frac_current_selection

    return optimal_selection


def knapsack_fractional_bruteforce(profits, weights, max_capacity):
    length = len(profits)

    current_max_profit = 0

    selected_indices = [0 for _ in range(length)]

    lst = list(itertools.product([0, 1], repeat=len(profits)))

    for val in lst:
        current_selected = list(val)

        frac_current_selection = fill_remaining_with_best_weights(profits, weights, max_capacity, current_selected)

        if sum(list_scaler_multiply(weights, frac_current_selection)) <= max_capacity:
            current_profit = sum(list_scaler_multiply(profits, frac_current_selection))

            if current_profit > current_max_profit:
                current_max_profit = current_profit
                selected_indices = frac_current_selection

    return selected_indices


if __name__ == "__main__":
    profits = [10, 15, 20]
    weights = [50, 200, 300]
    max_capacity = 400

    ret = knapsack_fractional_bruteforce(profits, weights, max_capacity)
    print(ret)
