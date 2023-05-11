from setuptools import find_packages, setup
from typing import List

hyphen_e='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "")for req in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)

    return requirements

        

setup(
    name='tempML',
    version='0.0.1',
    author='Ritesh',
    author_email='riteshsharma.here@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
                           
)