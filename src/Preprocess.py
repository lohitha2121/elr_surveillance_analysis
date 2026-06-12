import os
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower().str.strip()
    return df


# =========================================================
# LOAD DATASETS
# =========================================================
def load_data():
    """
    Loads raw datasets from local data folder.
    """

    elr_path = os.path.join(BASE_DIR, "data/raw/elr_data.csv")
    facility_path = os.path.join(BASE_DIR, "data/raw/facility.csv")
    district_path = os.path.join(BASE_DIR, "data/raw/county_district_mapping.csv")
    lab_path = os.path.join(BASE_DIR, "data/raw/lab_results.csv")

    elr = pd.read_csv(elr_path)
    facility = pd.read_csv(facility_path)
    district = pd.read_csv(district_path)
    lab = pd.read_csv(lab_path)

    # standardize schema
    elr = clean_columns(elr)
    facility = clean_columns(facility)
    district = clean_columns(district)
    lab = clean_columns(lab)

    return elr, facility, district, lab


# =========================================================
# PREPARE ELR DATASET
# =========================================================
def prepare_elr(elr, facility, district):

    elr = clean_columns(elr)
    facility = clean_columns(facility)
    district = clean_columns(district)

    # -------------------------
    # Merge facility table
    # -------------------------
    df = elr.merge(
        facility,
        on="clia_id",
        how="left",
        suffixes=("_elr", "_fac")
    )

    
    if "facility_name_fac" in df.columns:
        df["facility_name"] = df["facility_name_fac"]
    elif "facility_name_elr" in df.columns:
        df["facility_name"] = df["facility_name_elr"]

    
    if "county_fac" in df.columns:
        df["county"] = df["county_fac"]
    elif "county_elr" in df.columns:
        df["county"] = df["county_elr"]

    # -------------------------
    # Merge district mapping
    # -------------------------
    df = df.merge(
        district[["county", "district"]],
        on="county",
        how="left",
        suffixes=("", "_dist")
    )

    # Final cleanup for district
    if "district_dist" in df.columns:
        df["district"] = df["district_dist"]

    return df


# =========================================================
# ADD TIME FEATURES
# Used for trend analysis and reporting breakdowns
# =========================================================
def add_time_features(df):

    df = df.copy()

    if "insert_date" in df.columns:
        df["insert_date"] = pd.to_datetime(df["insert_date"], errors="coerce")

        df["report_date"] = df["insert_date"].dt.date
        df["report_week"] = df["insert_date"].dt.isocalendar().week
        df["report_month"] = df["insert_date"].dt.month
        df["report_year"] = df["insert_date"].dt.year

    return df


# =========================================================
# FULL PIPELINE 
# =========================================================
def build_elr_dataset():
    """
    End-to-end pipeline:
    Load → Prepare → Feature engineering
    """

    elr, facility, district, lab = load_data()

    df = prepare_elr(elr, facility, district)
    df = add_time_features(df)

    return df, lab