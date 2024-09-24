from dagster import (
    Definitions,
    load_assets_from_package_module,
)

from . import assets

# Load assets from the 'assets' module
loaded_assets = load_assets_from_package_module(assets)

# Define the Dagster Definitions
defs = Definitions(
    assets=loaded_assets,
)
