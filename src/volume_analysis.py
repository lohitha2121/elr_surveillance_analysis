import pandas as pd


def daily_volume(df):
    return (
        df.groupby("insert_date")["msg_control_id"]
        .count()
        .reset_index()
        .rename(columns={"msg_control_id": "message_count"})
    )


def facility_volume(df):

    required = ["facility_name", "clia_id", "msg_control_id"]

    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    return (
        df.groupby(["facility_name", "clia_id"])["msg_control_id"]
        .count()
        .reset_index()
        .rename(columns={"msg_control_id": "message_count"})
    )


def district_volume(df):

    if "district" not in df.columns:
        raise ValueError(f"district missing. Columns: {df.columns.tolist()}")

    return (
        df.groupby("district")["msg_control_id"]
        .count()
        .reset_index()
        .rename(columns={"msg_control_id": "message_count"})
    )