
def knapsack_0_1_dynamic(profits, weights, max_capacity):
    # storing the previously calculated values in matrix
    memo = [[0 for _ in range(max_capacity + 1)] for _ in range(len(profits) + 1)]

    def knapsack_0_1_dynamic_helper(idx, cap):
        if idx <= 0 or cap <= 0:
            return 0

        if memo[idx][cap] != 0:
            return memo[idx][cap]

        if weights[idx - 1] > cap:
            calculated_profit = knapsack_0_1_dynamic_helper(
                idx - 1, cap
            )  # not taking the element which cannot fit

        else:
            calculated_profit = max(
                profits[idx - 1]
                + knapsack_0_1_dynamic_helper(
                    idx - 1, cap - weights[idx - 1]
                ),  # taking the nth element
                0
                + knapsack_0_1_dynamic_helper(
                    idx - 1, cap
                ),  # not taking the nth element
            )

        memo[idx][cap] = calculated_profit
        return calculated_profit

    return knapsack_0_1_dynamic_helper(len(profits), max_capacity)


if __name__ == "__main__":
    # profits = [15, 10, 20]
    # weights = [200, 100, 300]
    # max_capacity = 400


    weights = [1, 3, 4, 5]
    profits = [1, 4, 5, 7]
    max_capacity = 7
    optimal_combination = [0, 1, 1, 0]
    expected = 9


    ret = knapsack_0_1_dynamic(profits, weights, max_capacity)
    print(ret)
