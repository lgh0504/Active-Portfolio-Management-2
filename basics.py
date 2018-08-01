from math import sqrt

'''
Active management is forecasting.

Strategy: separate forecasting into risk and return.
Investors care about *active* risk/return relative to a benchmark.
We use *residual* return: return uncorrelated with benchmark return.

INFORMATION RATIO (IR): ratio of expected residual return to its volatility
(both annual). Higher IR means more active management opportunities.

PREFERENCE: we prefer high residual return and low residual risk.

VALUE ADDED: residual return - quadratic penalty on residual risk.
Equivalent to residual return - linear penalty on residual variance.
A.K.A. risk-adjusted expected return.
Max possible value added is proportional to the squared information ratio.
The information ratio measures active management opportunities.
The squared information ratio measures potential to add value.

FUNDAMENTAL LAW OF ACTIVE MANAGEMENT: IR = IC * sqrt(BR)
'''
def information_ratio(ic, br):
    return ic * sqrt(br)
'''
INFORMATION COEFFICIENT (IC): our skill in forecasting residual return,
i.e. correlation between forecasts and the eventual returns.
BREADTH (BR): number of times per year we can use our skill.

Portfolio management foundations:
return, risk, benchmarks, preferences, information ratios.
*Active* management demands our forecasts of expected return to be
different from the consensus.

Forecasting takes raw signals of returns and outputs predictions.
ALPHA: forecast of residual return.
ALPHA = VOLATILITY * IC * SCORE
'''
def alpha(volatility, ic, score):
    return volatility * ic * score
'''
Volatility: residual volatility.
IC: correlation between scores and returns.
Score: measure of how we feel about an asset
(standardised: mean 0, unit standard deviation).
'''
