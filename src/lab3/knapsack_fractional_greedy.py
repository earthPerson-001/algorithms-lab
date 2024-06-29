from src.lab3.utils import list_scaler_multiply


def knapsack_fractional_greedy(profits, weights, max_capacity):

    # keeping track of indices
    # sorting in descending order
    sorted_profits_and_weights = sorted(
        list(zip(profits, weights, [i for i in range(len(profits))])),
        key=lambda x: x[0] / x[1],  # arranging in descending order of profits/weight
        reverse=True,
    )
    already_selected = [0 for _ in range(len(profits))]

    for profit, weight, index in sorted_profits_and_weights:
        remaining_weight = max_capacity - sum(
            list_scaler_multiply(already_selected, weights)
        )

        if remaining_weight <= 0:
            break

        current_selected = already_selected.copy()
        current_selected[index] = 1

        if sum(list_scaler_multiply(current_selected, weights)) > max_capacity:
            # adding the fraction of it which can fit
            current_selected[index] = remaining_weight / weight
        already_selected = current_selected

    return already_selected


if __name__ == "__main__":
    profits = [15, 10, 20]
    weights = [200, 100, 300]
    max_capacity = 400

    ret = knapsack_fractional_greedy(profits, weights, max_capacity)
    print(ret)
