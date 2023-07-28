from setuptools import setup, find_packages

try:
    with open("requirements.txt", encoding="utf-8") as r:
        requires = [i.strip() for i in r]
except FileNotFoundError:
    requires = ["httpx<=0.24.1", "websockets<=11.0.3"]
try:
    import pypandoc

    long_description = pypandoc.convert_file("README.md", "rst")
except (IOError, ImportError):
    long_description = open("README.md").read()


setup(
    name="swibots",
    version="1.3.15b0",
    packages=find_packages(exclude=["samples", "bots_impl", "docs"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/switchcollab/Switch-Bots-Python-Library",
    description="Bots Library for Switch",
    author="switchadmin",
    author_email="support@switch.pe",
    license="LGPLv3",
    python_requires=">=3.10",
    install_requires=requires,
)
