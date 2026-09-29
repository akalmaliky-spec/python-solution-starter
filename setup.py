"""Setup configuration for the Python solution project."""

from setuptools import setup

setup(
    name="python-solution",
    version="0.1.0",
    description="Minimal Python starter kit with solution code template",
    author="Akram Almaliky",
    url="https://github.com/akalmaliky-spec/python-solution-starter",
    py_modules=["main", "utils", "config", "logger"],
    python_requires=">=3.8",
    install_requires=[
        # Add dependencies here
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
