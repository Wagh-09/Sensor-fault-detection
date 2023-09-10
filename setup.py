from setuptools import find_packages, setup
from typing import List

def get_requirements()->list[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str]= []

    """
    Write code to read requirements.txt file and append each requiremnts in list variable
    """
    return requirement_list
setup(

    name="sensor",
    version="0.0.1",
    author="kirti",
    author_email="kirtiwagh09@gmail.com",
    packages= find_packages(),
    install_requires=get_requirements(),#["pymongo==4.2.0"]
)