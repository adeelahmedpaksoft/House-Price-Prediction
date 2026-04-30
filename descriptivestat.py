import pandas as pd
import numpy as np

def descriptive_statistics(data, column):
    sample = data[column]
    desc = {
        "Mean": np.mean(sample),
        "Median": np.median(sample),
        "Standard Deviation": np.std(sample),
        "Minimum": np.min(sample),
        "Maximum": np.max(sample),
        "Count": sample.count()
    }
    return pd.DataFrame(desc, index=[column])
