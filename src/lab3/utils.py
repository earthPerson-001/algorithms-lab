def list_scaler_multiply(list1, list2):
    out = [0 for _ in range(len(list1))]
    for i in range(len(list1)):
        out[i] = list1[i] * list2[i]

    return out
