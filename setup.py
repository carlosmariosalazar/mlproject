from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = 'e .'

def get_requirements(file_name: str) -> List[str]:
    
    requirements = []
    
    with open(file_name, 'r') as file_obj:
        requierements = file_obj.readlines() 
        requierements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requierements:
            requierements.remove(HYPHEN_E_DOT)
    
    return requierements

setup(
    name = "mlproject",
    version = "0.0.1",
    author = "Carlos Mario Salazar",
    author_email = "carlosmsdiaz@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)