from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    graph_asset,
    load_assets_from_package_module,
    op,
    with_source_code_references,
)

from . import assets

daily_refresh_schedule = ScheduleDefinition(
    job=define_asset_job(name="all_assets_job"), cron_schedule="0 0 * * *"
)


@op
def foo_op():
    return 5


@graph_asset
def my_asset():
    return foo_op()


my_assets = with_source_code_references(
    [
        my_asset,
        *load_assets_from_package_module(assets),
    ]
)

defs = Definitions(
    assets=load_assets_from_package_module(assets), schedules=[daily_refresh_schedule]
)

defs = Definitions(
    assets=my_assets,
    schedules=[daily_refresh_schedule],
)
