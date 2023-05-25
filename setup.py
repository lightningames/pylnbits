#!/usr/bin/env python
from setuptools import find_packages, setup

if __name__ == "__main__":
    # setuptools.setup()
    VERSION = "0.0.6"

    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()

    install_requires = open("requirements.txt").readlines()

    setup(
        name="pylnbits",
        version=VERSION,
        author="bitkarrot",
        description="python library for lnbits",
        maintainer="Lightning Games",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/lightningames/pylnbits",
        project_urls={
            "Bug Tracker": "https://github.com/lightningames/pylnbits/issues",
        },
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        packages=find_packages(),
        install_requires=install_requires,
        include_package_data=True,
        python_requires=">=3.8",
    )
