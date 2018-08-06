import numpy as np

def alpha(ret_p, ret_b):
    '''
    Alpha is a measure of returns relative to a benchmark (market), i.e. active
    return.

    ALPHA = Rp - Rb
    '''
    return np.subtract(ret_p, ret_b)

def beta(ret_p, ret_b):
    '''
    Beta is a measure of volatility relative to a benchmark (market).

    BETA = Cov(Rp, Rb) / Var(Rb)
    '''
    covariance = np.cov(ret_p, ret_b)[0][1]
    benchmark_variance = np.var(ret_b)
    return covariance / benchmark_variance

def information_ratio(ic, br):
    '''
    Information ratio is the ratio of expected residual return to its
    volatility.

    IR = IC * sqrt(BR)
    (fundamental law of active management)
    Information Coefficient (IC): our skill in forecasting residual return,
    i.e. correlation between forecasts and the eventual returns.
    Breadth (BR): number of times per year we can use our skill.
    '''
    return ic * br ** 0.5

def alpha_theoretical(volatility, ic, score):
    '''
    Alpha is a measure of returns relative to a benchmark (market).

    ALPHA = VOLATILITY * IC * SCORE
    Volatility: residual volatility.
    IC: correlation between scores and returns.
    Score: measure of how we feel about an asset
    (standardised: mean 0, unit standard deviation).
    '''
    return volatility * ic * score
