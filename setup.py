from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1.0',
    author='Ayman Elsayeed',
    description='A small example package',
    packages=find_packages(include=['python-package', 'python-package.*']),
    install_requires=['numpy', 'pandas', 'scikit-learn'],
    python_requires='>=3.6',
)