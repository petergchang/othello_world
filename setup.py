from setuptools import setup, find_packages

setup(
    name="othello_world",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pgnparser==1.0",
    ],
)
