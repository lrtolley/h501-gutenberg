import pandas as pd
import numpy as np
import seaborn as sns

gutenberg_authors = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
gutenberg_languages = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
gutenberg_metadata = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
gutenberg_subjects = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')

def list_authors(by_languages=False, alias=False):
    """Return authors sorted by language count or raw alias list."""
    
    # Drop NaNs from alias
    authors_clean = gutenberg_authors.dropna(subset=['alias'])

    # Merge authors → metadata → languages
    merged = authors_clean.merge(gutenberg_metadata, on='author_id', how='inner')
    merged = merged.merge(gutenberg_languages, on='book_id', how='inner')

    # Count number of languages per alias
    lang_counts = merged.groupby('alias')['language'].nunique().reset_index(name='language_count')

    # Sort by language count if requested
    if by_languages:
        lang_counts = lang_counts.sort_values(by='language_count', ascending=False)

    # Return list of aliases or full DataFrame
    if alias:
        return lang_counts['alias'].tolist()
    else:
        return lang_counts
