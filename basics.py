from math import sqrt

def information_ratio(ic, br):
    '''
    Fundamental law of active management: IR = IC * sqrt(BR)
    Information Ratio (IR): ratio of expected residual return to its volatility.
    Information Coefficient (IC): our skill in forecasting residual return,
    i.e. correlation between forecasts and the eventual returns.
    Breadth (BR): number of times per year we can use our skill.
    '''
    return ic * sqrt(br)

def alpha(volatility, ic, score):
    '''
    ALPHA = VOLATILITY * IC * SCORE
    Volatility: residual volatility.
    IC: correlation between scores and returns.
    Score: measure of how we feel about an asset
    (standardised: mean 0, unit standard deviation).
    '''
    return volatility * ic * score
