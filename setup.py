#!/usr/bin/python3
from setuptools import setup, find_packages
__version__="0.0.0"

def get_long_description():
    with open("README.md") as f:
        long_description = f.read()

    try:
        import github2pypi

        return github2pypi.replace_url(
            slug="pk-628996/pyrogramhelper", content=long_description
        )
    except Exception:
        return long_description

setup(
    name="pyrogramhelper",
    version=f"{__version__}",
    packages=['pyrogramhelper'],
    py_modules=['pyrogramhelper'],
    description="A module for some common things",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    download_url=f'https://github.com/pk-628996/pyrogramhelper/archive/refs/tags/v{__version__}-alpha.zip',
    url='https://github.com/pk-628996/pyrogramhelper',
    license="MIT",
    install_requires=['gdown','pytube','aiohttp','hachoir','pyrogram','convopyro'],
    entry_points={"console_scripts": ["pyrogramhelper=pyrogramhelper.cli:main"]},
)
