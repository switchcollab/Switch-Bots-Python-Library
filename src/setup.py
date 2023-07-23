from setuptools import setup, find_packages

try:
    with open("requirements.txt", encoding="utf-8") as r:
        requires = [i.strip() for i in r]
except:
        requires = ["httpx==0.23.3", "websockets==10.4"]

try:
    import pypandoc

    long_description = pypandoc.convert_file("README.md", "rst")
except (IOError, ImportError):
    long_description = open("README.md").read()


setup(
    name="swibots",
    version="1.3.10",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/switchcollab/Switch-Bots-Python-Library",
    description="Switch bot api",
    author="switchadmin",
    author_email="support@switch.pe",
    license="LGPLv3",
    python_requires=">=3.10",
    install_requires=requires,
)
