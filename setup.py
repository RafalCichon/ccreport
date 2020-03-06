import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ccreport",
    version="1.0.10",
    description="Code coverage report for builds hosted on Azure DevOps.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/RafalCichon/ccreport",
    author="Rafał Cichoń",
    author_email="",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["azure-devops"],
    entry_points={
        "console_scripts": [
            "ccreport=ccreport.entrypoints.main:main",
        ]
    },
	python_requires='>=3.8',
)
