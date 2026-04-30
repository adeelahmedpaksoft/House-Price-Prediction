from scipy.stats import ttest_1samp

t_stat, p_value = ttest_1samp(random_sample["SalePrice"], 180000)
