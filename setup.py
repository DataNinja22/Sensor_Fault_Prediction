from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    requirements_list:List[str]=[]
    return requirements_list 
    


#Information about the project
setup(
name="Fault_Detection in APS",
version="0.0.1",
author="Shyam Mohan Tripathi",
author_email="tripathishyam22@gmail.com",
packages=find_packages(),  #checks the project for the packages
install_requires=get_requirements(),
)