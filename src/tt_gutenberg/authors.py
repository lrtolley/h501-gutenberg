import pandas as pd
import numpy as np


gutenberg_authors = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
gutenberg_languages = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
gutenberg_metadata = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
gutenberg_subjects = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')

#gutenberg_authors['gutenberg_id'] = gutenberg_authors['gutenberg_author_id']
#making a new column for gutenberg_id to match with gutenberg_languages - didn't realise these were different ids

gutenberg_merged = pd.merge(gutenberg_authors, gutenberg_metadata, on='gutenberg_author_id', how='inner')
gutenberg_merged = pd.merge(gutenberg_merged, gutenberg_subjects, on='gutenberg_id', how='inner')
gutenberg_merged = pd.merge(gutenberg_merged, gutenberg_languages, on='gutenberg_id', how='inner')
gutenberg_merged = gutenberg_merged.dropna() #dropping where there are NaN values to get a clean list

#print(gutenberg_merged.head()) #checking that the merges worked

def list_authors(by_languages=False, alias=False):
  gutenberg_sorted = gutenberg_merged.sort_values(by='author_x') #because there were two 'author' columns, they got renamed
  #return gutenberg_sorted[['alias', 'language']]
  if by_languages:
    gutenberg_sorted = gutenberg_sorted.sort_values(by='total_languages')
    return gutenberg_sorted[['alias']]
    # Return list of aliases or whoopsie message
  if alias:
      return gutenberg_sorted['alias'].sort_values(by='alias')
  else:
      return "Please set by_languages or alias = True"

list_authors(by_languages=True, alias=True)
