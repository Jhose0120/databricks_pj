import pytest
import pandas as pd

from covid_analysis.transforms import (
    filter_country,
    pivot_and_clean,
    clean_spark_cols
)


@pytest.fixture
def raw_input_df() -> pd.DataFrame:
    """
    Create a basic version of the input dataset for testing, including NaNs.
    """
    return pd.read_csv("tests/testdata.csv")


@pytest.fixture
def colnames_df() -> pd.DataFrame:
    return pd.DataFrame(
        data=[[0, 1, 2, 3, 4, 5]],
        columns=[
            "Daily ICU occupancy",
            "Daily ICU occupancy per million",
            "Daily hospital occupancy",
            "Daily hospital occupancy per million",
            "Weekly new hospital admissions",
            "Weekly new hospital admissions per million",
        ],
    )


def test_filter(raw_input_df):
    """
    Make sure the filter works as expected.
    """
    filtered = filter_country(raw_input_df)
    assert filtered["iso_code"].drop_duplicates().iloc[0] == "USA"


def test_pivot(raw_input_df):
    """
    The test data has NaNs for Daily ICU occupancy; this should get filled to 0.
    """
    pivoted = pivot_and_clean(raw_input_df, 0)
    assert pivoted.iloc[0, "Daily ICU occupancy"] == 0


def test_clean_cols(colnames_df):
    """
    Test column cleaning.
    """
    cleaned = clean_spark_cols(colnames_df)
    cols_w_spaces = cleaned.filter(regex=" ")
    assert cols_w_spaces.empty
