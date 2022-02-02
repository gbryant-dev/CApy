import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="CApy",
    version="0.0.1",
    author="George Bryant",
    author_email="gbryant@hotmail.co.uk",
    description="Python wrapper for Cognos Analytics REST API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/gbryant-dev/CApy",
    keywords=['Cognos', 'Cognos Analytics', 'CA', 'TM1', 'Planning Analytics', 'REST API'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    install_requires=[
        'requests'
    ],
    python_requires='>=3.6'
)