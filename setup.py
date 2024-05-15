from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e.'

def get_requirements(file_path:str) -> list[str]:
    '''
    this function will return the list of requirements
    '''
    requirememts = []
    with open(file_path) as file_obj:
        requirememts = file_obj.readlines()
        [reg.replace("\n"," ") for reg in requirememts]
        
        if HYPEN_E_DOT in requirememts:
            requirememts.remove(HYPEN_E_DOT)
            
    return requirememts           
            

setup(
name ='mlproject',
version ='0.0.1',
author ='karthik',
author_email ='premaramkarthik99@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
    
)