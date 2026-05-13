from setuptools import setup, find_packages

setup(
    name="allen-lab-rml",
    version="0.1.0",
    description="RML + CGCS framework for Allen Lab Trisomy 21 research",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "scipy>=1.10.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
    ],
)
