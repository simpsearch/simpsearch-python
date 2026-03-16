from setuptools import setup, find_packages

setup(
    name="simpsearch",
    version="0.1.0",
    description="Lightweight search and text extraction library",
    packages=find_packages(),
    install_requires=["requests"],
)