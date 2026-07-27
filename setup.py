import os
from setuptools import setup, find_packages

# long_description from readme if exists
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
long_description = ""
if os.path.exists(readme_path):
    with open(readme_path, encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="latencyhist",
    version="0.2.1",
    author="Aleksey",
    description="Terminal latency histograms from stdin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/local/latencyhist",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
        "numpy>=1.20.0", # added for faster percentile math
    ],
    entry_points={
        "console_scripts": [
            "latencyhist=latencyhist.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
    ],
    python_requires=">=3.8",
)
