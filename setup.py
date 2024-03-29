import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Fluidity",
    version="0.0.1",
    author="CyroCoders",
    author_email="pypi@cyrocoders.dev",
    description="Fluidity Is An Interpreted Smart Contract Language For Blockchains Based On Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CyroCoders/Fluidity",
    project_urls={
        "Bug Tracker": "https://github.com/CyroCoders/Fluidity/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
    install_requires=[
    ]
)