from setuptools import find_packages,setup
from typing import List

hy_e_dot = "-e ."

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hy_e_dot in requirements:
            requirements.remove(hy_e_dot)


    return requirements


setup(

    name = "Regression", version = '1.0', author= "Aman Mishra", author_email = "aman.mishra23@outlook.com",
    install_requires = get_requirements("requirements.txt"), packages = find_packages()
)