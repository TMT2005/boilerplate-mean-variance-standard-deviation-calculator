import numpy as np

def calculate(list):
matrix = np.array(list).reshape(3, 3)

    meanAxis1 = np.mean(matrix, axis=0).tolist()
    Var1 = np.var(matrix, axis=0).tolist()
    std1 = np.std(matrix, axis=0).tolist()
    max1 = np.max(matrix, axis=0).tolist()
    min1 = np.min(matrix, axis=0).tolist()
    sum1 = np.sum(matrix, axis=0).tolist()
    
    meanAxis2 = np.mean(matrix, axis=0).tolist()
    Var2 = np.var(matrix, axis=1).tolist()
    std2 = np.std(matrix, axis=1).tolist()
    max2 = np.max(matrix, axis=1).tolist()
    min2 = np.min(matrix, axis=1).tolist()
    sum2 = np.sum(matrix, axis=1).tolist()

    meanTotal = np.mean(matrix)
    VarTotal = np.var(matrix)
    stdTotal = np.std(matrix)
    maxTotal = np.max(matrix)
    minTotal = np.min(matrix)
    sumTotal = np.sum(matrix)

    calculations = {
    'mean': [meanAxis1, meanAxis2, meanTotal],
    'variance': [Var1, Var2, VarTotal],
    'standard deviation': [std1, std2, stdTotal],
    'max': [max1, max2, maxTotal],
    'min': [min1, min2, minTotal],
    'sum': [sum1, sum2, sumTotal]
    }


    return calculations