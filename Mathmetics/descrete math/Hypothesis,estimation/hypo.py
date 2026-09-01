#testing hypothesis for ml

import numpy as np
import pandas as pd


np.random.seed(0)
population_mean = 50
population_std = 10
sample_size = 30

population_data = np.random.normal(population_mean, population_std, 1000)
population_df = pd.DataFrame(population_data, columns=['Value'])

population_df['Type'] = 'Population'
population_df['Mean'] = population_mean

print("Population Mean:", population_df['Value'].mean())\

"""there are multiple types of hypothetis testing, including tabular, calculations, comparisation 
"""
