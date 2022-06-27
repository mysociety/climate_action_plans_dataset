import climate_action_plans_dataset

import pytest
import pandas as pd
import numpy as np
from pathlib import Path

from data_common.dataset import get_dataset_df


top_level = Path(__file__).parent.parent
raw_csv_path = top_level / "data" / "raw" / "councils_sheet.csv"
processed_csv_path = (
    top_level / "data" / "packages" / "climate_action_plans" / "councils_plans.csv"
)


def get_df():
    return pd.read_csv(processed_csv_path)


def get_la_dataset():
    """
    Get future version of la dataset
    """
    return get_dataset_df(
        "uk_local_authority_names_and_codes",
        "uk_la_future",
        "latest",
        "uk_local_authorities_future.csv",
    )


def test_column_names_are_snake_case():
    """
    ensure that column names are snake_case and do not contain spaces or hyphens
    """
    df = get_df()
    for col in df.columns:
        assert " " not in col, f"column name {col} contains spaces"
        assert "-" not in col, f"column name {col} contains hyphens"
        assert col.islower(), f"column name {col} is not lowercase"


def test_valid_scope():
    """
    Check the scope column only has null, 'Whole area' or 'Council only' as values.
    """
    df = get_df()
    allowed_values = ["Whole area", "Council only", np.NAN]

    for n, scope in df["scope"].iteritems():
        assert scope in allowed_values, f"scope is not valid for row {n}, {scope}"


def test_has_councils():
    """
    Check that all values in the local_authority_code column are populated
    """
    df = get_df()

    for n, row in df.iterrows():
        assert (
            row["local_authority_code"] is not np.NAN
        ), f"local_authority_code is not populated for row {row['council']}"


def test_has_valid_councils():
    df = get_df()
    la_dataset = get_la_dataset()
    valid_councils = la_dataset["local-authority-code"].tolist()
    for n, row in df.iterrows():
        assert (
            row["local_authority_code"] in valid_councils
        ), f"local_authority_code is not valid for row {row['council']}"
