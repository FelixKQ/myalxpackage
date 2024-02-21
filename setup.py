from setuptools import setup, find_packages

setup(
    name= 'mypackage',
    version= '0.1', 
    packages=find_packages(exclude=['tests*']),
    license= 'MIT',
    description= 'EDSA example python package', 
    long_description=open('ReadMe.md').read(),
    install_requires=['numpy'],
    url= 'https://github.com/<username>/ <package-name>',
    author='Felix Kusi Quainoo',
    author_email='kusilex1@gmail.com'
)

