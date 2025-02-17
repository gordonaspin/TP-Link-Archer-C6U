import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tplinkrouterc6u",
    version="3.2.0",
    author="Alex Erohin",
    author_email="alexanderErohin@yandex.ru",
    description="TP-Link Router API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexandrErohin/TP-Link-Archer-C6U",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests', 'pycryptodome', 'macaddress'],
    python_requires='>=3.10',
)