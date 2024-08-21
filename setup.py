from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


# setup function: Central feature of setuptools, used to configure various aspects of the package.

setup(
    name = 'mlproject', # Specifies the name of the package. This is the name that users will use to install the package via pip.
    version = '0.0.1', # The version of the package. This is used to indicate the current state of the package and manage dependencies.
    author = 'SupritPatil',
    author_email = 'suprit202@gmail.com',
    packages = find_packages(), # automatically discovers all packages and subpackages (a directory with an __init__.py)
    install_requires = get_requirements('requirements.txt'), # A list of dependencies that setuptools will attempt to install alongside your package.
)