from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prokit",  
    version="0.1.2",
    author="Sarah Ali",
    author_email="alsayedsarah01@gmail.com",
    description="Lightweight Python library to fetch and analyze protein sequences from UniProt.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/prokit",
    packages=find_packages(),
    install_requires=[
        "requests>=2.30",
        "pandas>=2.0",
        "ipython>=8.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
