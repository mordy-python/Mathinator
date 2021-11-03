import setuptools
from mathinator import version
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Mathinator",
    version=version,
    author="Israel Waldner",
    author_email="imky171@gmail.com",
    description="A command line tool to do hard math quickly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mordy-python/Mathinator",
    project_urls={
        "Bug Tracker": "https://github.com/mordy-python/Mathinator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
		install_requires = [
			'click'
		],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)