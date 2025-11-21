import pandas as pd
import numpy as np


gutenberg_authors = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
gutenberg_languages = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
gutenberg_metadata = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
gutenberg_subjects = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')

gutenberg_authors['gutenberg_id'] = gutenberg_authors['gutenberg_author_id']
#making a new column for gutenberg_id to match with gutenberg_languages

gutenberg_merged = pd.merge(gutenberg_authors, gutenberg_languages, on='gutenberg_id', how='inner')
gutenberg_merged = gutenberg_merged.dropna() #dropping where there are NaN values to get a clean list

def list_authors(by_languages=False, alias=False):
  gutenberg_sorted = gutenberg_merged.sort_values(by=['alias'])
  return gutenberg_sorted[['alias', 'language']]

