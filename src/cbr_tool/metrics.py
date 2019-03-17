import numpy as np
import pandas as pd


def count_rows_null(df):
    return df.isnull().shape(0)


def median(col):
    return np.median(col.values)


def average(col):
    return np.average(col.values)


""" All types """


def count_not_null(col):
    return np.count_nonzero(~np.isnan(data))


def count_null(col):
    return col.size - count_not_null(col)


def count_freqs(col):
    return 1.2


def count_nans(col):
    return 0.9
