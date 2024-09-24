from setuptools import find_packages, setup

setup(
    name="ndr-dagster",
    packages=find_packages(),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "boto3",
        "pandas",
        "matplotlib",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
