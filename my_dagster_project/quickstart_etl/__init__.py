from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    graph_asset,
    load_assets_from_package_module,
    op,
)

from . import assets

# Define a simple schedule
daily_refresh_schedule = ScheduleDefinition(
    job=define_asset_job(name="all_assets_job"),
    cron_schedule="0 0 * * *",
)

# Define an example op and asset
@op
def foo_op():
    return 5

@graph_asset
def my_asset():
    return foo_op()

# Load assets from the 'assets' module
loaded_assets = load_assets_from_package_module(assets)

# Combine your custom asset with loaded assets if needed
# If you don't need to add custom assets, you can directly use 'loaded_assets'
# For demonstration, we'll include 'my_asset' as well
all_assets = loaded_assets + [my_asset]

# Define the Dagster Definitions
defs = Definitions(
    assets=all_assets,
    schedules=[daily_refresh_schedule],
)
