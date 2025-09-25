"""Small utilities to load tidyTuesday Gutenberg datasets.

The module avoids performing network I/O at import time; call functions to load data.
"""
from typing import List

import pandas as pd

# Remote CSV sources (tidytuesday 2025-06-03)
_AUTHORS_URL = (
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
)
_LANGUAGES_URL = (
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
)
_METADATA_URL = (
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
)
_SUBJECTS_URL = (
    "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv"
)


def load_all() -> dict:
    """Load all Gutenberg tidytuesday CSVs and return a dict of DataFrames.

    Returns:
        dict: keys 'authors', 'languages', 'metadata', 'subjects'
    """
    authors = pd.read_csv(_AUTHORS_URL)
    languages = pd.read_csv(_LANGUAGES_URL)
    metadata = pd.read_csv(_METADATA_URL)
    subjects = pd.read_csv(_SUBJECTS_URL)
    return {
        "authors": authors,
        "languages": languages,
        "metadata": metadata,
        "subjects": subjects,
    }


def list_aliases() -> List[str]:
    """Return the list of author aliases from the authors dataset.

    This function lazily loads the authors CSV.
    """
    df = pd.read_csv(_AUTHORS_URL)
    if "alias" in df.columns:
        return df["alias"].dropna().astype(str).tolist()
    # fallback: try 'aliases' column
    if "aliases" in df.columns:
        return df["aliases"].dropna().astype(str).tolist()
    return []
