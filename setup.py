import io
from pkgutil import walk_packages
from setuptools import setup
from pathlib import Path

import wesanderson.__package_info__ as package_info

def find_packages(path):
    # This method returns packages and subpackages as well.
    return [name for _, name, is_pkg in walk_packages([path]) if is_pkg]


def read_file(filename):
    with io.open(filename) as fp:
        return fp.read().strip()


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(
    name=package_info.name,
    packages=list(find_packages('.')),
    version=package_info.__version__,
    author=package_info.pypi_author,
    author_email=package_info.pypi_author_email,
    description=package_info.pypi_description,
    long_description=package_info.pypi_description,
    long_description_content_type="text/markdown",
    setup_requires=read_requirements('requirements.txt'),
    install_requires=read_requirements('requirements.txt'),
    url="",
    include_package_data=True,
    keywords='color, wesanderson',
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        "Operating System :: OS Independent",
        'Natural Language :: English'
    ],
)
