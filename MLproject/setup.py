from setuptools import find_packages, setup

from typing import List

def get_requirements(file:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        

setup(
    name="mlproject",
    version='0.0.1',
    author ='chandara',
    author_email='guruchandu4@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

