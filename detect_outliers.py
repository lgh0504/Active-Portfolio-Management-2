import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def clean(file_path, z = 3):
    '''
    Simple tool for detecting outliers in incoming time-series price data and
    removing them.

    Use: clean(file_path_as_string, OPTIONAL:z_score)

    Reads csv in format:
    Date,Price
    date1,price1
    date2,price2
    ...
    Outputs in same format. Also plots orginal data alongside cleaned data.

    Assumes the first 11 data points are reasonable - inspect them manually.
    Drop round-trip precision in read_csv for speed over accuracy.

    This tool uses z-standard-deviations-from-mean of recent price changes to
    detect anomalous data. An alternative would be a percentile-based approach,
    i.e. marking as outlier if not in range [LQ - 1.5 * IQR, UQ + 1.5 * IQR].
    '''
    df = pd.read_csv(file_path, float_precision = 'round_trip')
    plot_original = (df.plot(title = 'Original data', x = 'Date', y = 'Price')
                     .figure)
    plt.draw()

    print('Outliers:')
    outlier_indices = []
    for idx, item in df.Price.iteritems():
        if idx > 10:
            recent_changes = np.absolute(np.subtract(df.Price[idx - 10 : idx],
                             df.Price[idx - 11 : idx - 1]))
            if (abs(item - df.Price[idx - 1]) >
                recent_changes.mean() + z * recent_changes.std()):
                print('{} at {}'.format(df.Date[idx], df.Price[idx]))
                outlier_indices.append(idx)

    if not outlier_indices:
        print('none.')
    else:
        df = df.drop(outlier_indices)
        df.to_csv('cleaned_data.csv', index = False)
        plot_clean = (df.plot(title = 'Cleaned data', x = 'Date', y = 'Price')
                      .figure)
        plt.show()
