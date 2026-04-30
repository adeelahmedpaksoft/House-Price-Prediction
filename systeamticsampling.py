k = len(df) // 150
systematic_sample = df.iloc[::k]
descriptive_statistics(systematic_sample, "SalePrice")
