from setuptools import setup, find_packages

setup(
    name="hsha",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "hsha = hsha.main:main", 
        ],
    },
    install_requires=[],
    author="Med Boussalem",
    description="A simple command-line tool to create a predefined file structure.",
)
