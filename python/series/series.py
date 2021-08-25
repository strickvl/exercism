def slices(series, length):
    if len(series) == 0:
        raise ValueError("series is too small")
    elif length < 1:
        raise ValueError("length must be at least 1")
    elif length > len(series):
        raise ValueError("length cannot be greater than the series length")
    result = []
    idx = 0
    while idx <= (len(series) - length):
        slc = series[idx:(idx + length)]
        result.append(slc)
        idx += 1
    return result
