def calculateread(datas, pairs):
    S1 = datas[pairs[0]]
    S2 = datas[pairs[1]]
    models = statsmodels.OLS(S1, S2).fit()
    spreading = S1 - models.params[0] * S2
    return spreading


spreading = calculateread(data_info, pairing[0])