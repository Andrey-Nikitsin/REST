from pickle import TRUE
from xml.etree.ElementInclude import include
from setuptools import setup, find_packages
from pathlib import Path

BASE_DIR = Path(__file__).parent.absolute()


def get_version():
    with open(BASE_DIR / 'VERSION') as  file:
        return file.readline().strip()

def get_lisence():
    with open(BASE_DIR / 'LICENSE') as file:
        return file.read().strip()

def get_desc():
    with open(BASE_DIR / 'README.md') as file:
        return file.read().strip()

def get_packages():
    with open(BASE_DIR / 'requirements.txt') as file:
        return [package.strip() for package in file.readlines() if package]

VERSION = get_version()

setup(
    name= 'rest',
    version= VERSION,
    author= 'Andrey',
    author_email= 'secret@gmail.com',
    url= 'https://github.com/Andrey-Nikitsin/REST.git',
    license= get_lisence(),
    packages= find_packages(".", include=["rest"]),
    package_dir= {"" : "."},
    include_package_data= True,
    description= 'rest api',
    long_description= get_desc(),
    long_description_content_type= 'text/markdown',
    install_requires= get_packages(),
    python_require= '>=3.8',
    zip_safe= True,
    entry_points= {"console_scripts": ["rest_api = rest.app:run"]}, 
    classifiers= [
        "Development Status :: 3 - Alpha"
        if "dev" in VERSION
        else "Development Status :: 4 Beta"
        if "rc" in VERSION
        else "Development Status :: 5 Production/Stable"
    ]
)
