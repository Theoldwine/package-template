from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Dio_Images",
    version="0.0.2",
    author="theoldwine",
    author_email="sior@outlook.com",
    description="projeto python leitura da imagem",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://pypi.org/project/Dio-Images/",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)