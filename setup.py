from setuptools import setup, find_packages

setup(
    name='Loess-models',
    version='1.0.0',
    url='https://github.com/ChrisPayneHome/Loess-model.git',
    author='Christian Payne',
    author_email='',
    description='Implementation of Loess model',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)
