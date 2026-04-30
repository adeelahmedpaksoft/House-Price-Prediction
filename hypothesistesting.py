from scipy.stats import pearsonr, spearmanr

pearson_corr, p_value1 = pearsonr(df["GrLivArea"], df["SalePrice"])
spearman_corr, p_value2 = spearmanr(df["GrLivArea"], df["SalePrice"])
