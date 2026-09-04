from setuptools import setup, find_packages

setup(
    name="terminal-todo",
    version="1.0.0",
    author="Srikumar",
    description="A minimalist, native terminal-based task tracker written in Python.",
    packages=find_packages(),
    package_dir={"": "."},
    include_package_data=True,
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "todo=src.main:main",
        ],
    },
)

