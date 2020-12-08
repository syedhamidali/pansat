import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pansat",
    version="0.0.1",
    author="Julia Kukulies, Simon Pfreundschuh, Franz Kanngießer, Hannah Imhof",
    description="Download, extraction, remapping and analysis of satellite and climate data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SEE-MOF/pansat",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU Affero",
        "Operating System :: OS Independent",
    ],
    install_requires=["cryptography>=3.1", "numpy", "cdsapi", "requests", "xarray"],
    setup_requires=["pytest-runner"],
    tests_require=["sphinx_rtd_theme", "pytest", "appdirs", "scipy"],
    python_requires=">=3.8",
    entry_points={"console_scripts": ["pansat=pansat.download.commandline:download"]},
    include_package_data=True,
    package_data={"": ["*.ini"]},
)
