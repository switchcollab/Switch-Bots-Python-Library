from setuptools import setup, find_packages

try:
    import pypandoc

    long_description = pypandoc.convert_file("../README.md", "rst")
except (IOError, ImportError):
    long_description = open("../README.md").read()


setup(
    name="swibots",
    version="1.0.1",
    packages=find_packages(),
    long_description=long_description,
    description="Switch bot api",
)
