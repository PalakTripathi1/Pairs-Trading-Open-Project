
def integrated_pairs(data_info):
    n = data_info.shape[1]
    score = py.zeros((n, n))
    value= py.ones((n, n))
    key = data_info.columns
    pairing= []
    for i in range(n):
        for j in range(i+1, n):
            S1 = data_info[key[i]]
            S2 = data_info[key[j]]
            scores, values, _ = coint(S1, S2)
            score[i, j] = scores
            value[i, j] = values
            if values < 0.05:
                pairing.append((key[i], key[j]))
    return score, value, pairing

scores, values, pairing = integrated_pairs(data_info)
