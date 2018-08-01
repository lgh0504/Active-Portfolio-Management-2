from numpy import std

def risk(ret):
    '''
    Risk = standard deviation of return.
    The cost of risk is proportional to variance.
    '''
    return std(ret)
