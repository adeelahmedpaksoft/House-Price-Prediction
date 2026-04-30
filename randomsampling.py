df = pd.read_csv("house_prices.csv")
random_sample = df.sample(n=150, random_state=42)
descriptive_statistics(random_sample, "SalePrice")
