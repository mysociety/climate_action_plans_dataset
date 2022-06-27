import pandas as pd
import requests
from pathlib import Path


from data_common.dataset import get_dataset_df


PLANS_CSV_KEY = "1tEnjJRaWsdXtCkMwA25-ZZ8D75zAY6c2GOOeUchZsnU"
PLANS_CSV_SHEET_NAME = "Councils"

top_level = Path(__file__).parent.parent.parent
raw_csv_path = top_level / "data" / "raw" / "councils_sheet.csv"
processed_csv_path = (
    top_level / "data" / "packages" / "climate_action_plans" / "councils_plans.csv"
)


def get_google_sheet_as_csv(key: str, outfile: Path, sheet_name=None):
    """
    Download a google sheet as a csv to the path
    """
    sheet_url = f"https://docs.google.com/spreadsheets/d/{key}/gviz/tq?tqx=out:csv"
    if sheet_name is not None:
        sheet_url = f"{sheet_url}&sheet={sheet_name}"
    r = requests.get(sheet_url)
    with open(outfile, "wb") as out:
        out.write(r.content)


def get_plans_csv():
    get_google_sheet_as_csv(
        PLANS_CSV_KEY,
        raw_csv_path,
        sheet_name=PLANS_CSV_SHEET_NAME,
    )


# Replace the column header lines
def replace_headers():
    replace_csv_headers(
        raw_csv_path,
        [
            "council",
            "search_link",
            "unfound",
            "credit",
            "url",
            "date_retrieved",
            "time_period",
            "type",
            "scope",
            "status",
            "homepage_mention",
            "dedicated_page",
            "well_presented",
            "baseline_analysis",
            "notes",
            "plan_due",
            "title",
            "title_checked",
        ],
        outfile=processed_csv_path,
    )


def replace_csv_headers(
    csv_file: Path,
    new_headers: list[str],
    drop_empty_columns: bool = True,
    outfile: Path | None = None,
):
    """
    Sometimes google gives you bad headers
    This imposes local headers on the file.
    """
    if outfile is None:
        outfile = csv_file

    df = pd.read_csv(csv_file)
    if drop_empty_columns:
        df = df.dropna(axis="columns", how="all")

    df.columns = new_headers
    df.to_csv(outfile, index=False, header=True)


def fix_council_name(council: str) -> str:
    return (
        council.replace("council", "")
        .replace(" - unitary", "")
        .replace("(unitary)", "")
        .strip()
    )


def add_local_authority_code(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add the local-authority-code to the dataframe
    """

    name_to_code = get_dataset_df(
        repo="uk_local_authority_names_and_codes",
        package="uk_la_past_current",
        version="1",
        file="lookup_name_to_registry.csv",
    )
    df["council_lower"] = df["council"].str.lower().apply(fix_council_name)
    name_to_code["council_lower"] = (
        name_to_code["la-name"].str.lower().apply(fix_council_name)
    )
    df = df.merge(name_to_code, on="council_lower", how="left")

    # local-authority-code is in last position, move it to the start of the dataframe
    cols = list(df.columns)
    cols.insert(0, cols.pop(-1))
    df = df[cols]
    df = df.rename(columns={"local-authority-code": "local_authority_code"})
    df = df.drop(columns=["council_lower", "la-name"])
    return df


def process_csv():
    """
    Extra processing on columns to fix certain values
    """
    df = pd.read_csv(processed_csv_path)

    df = add_local_authority_code(df)

    df["scope"] = df["scope"].str.strip()

    df.to_csv(processed_csv_path, index=False)


def build():
    print("getting the csv")
    get_plans_csv()
    print("replacing headers")
    replace_headers()
    print("tidying values")
    process_csv()


if __name__ == "__main__":
    build()
