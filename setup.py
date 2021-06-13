from setuptools import find_packages, setup

setup(
    name="pylnbits-LNGAMES",
    version="0.0.1",
    package_dir={"": "pylnbits"},
    packages=find_packages(where="pylnbits"), 
    python_requires=">=3.8",)
