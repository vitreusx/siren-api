from setuptools import setup, find_packages

requires = ["flask==2.0.1"]

setup(
    name="siren",
    version="0.0.1",
    description="Siren API server",
    author="vitreusx",
    author_email="jakub_bednarz@protonmail.com",
    packages=find_packages(),
    requires=requires,
)
