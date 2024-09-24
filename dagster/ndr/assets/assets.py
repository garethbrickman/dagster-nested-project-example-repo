from dagster import asset

@asset
def my_asset() -> int:
    return 1
