from setuptools import setup, find_packages
 
VERSION = '2.2.0'
DESCRIPTION = "An API wrapper for both of the APIS I have made. "

setup(
    name='Mics_API_Wrapper',
    version=VERSION,
    author='Michael Parker',
    author_email='michaelrbparker@protonmail.com',
    url='https://github.com/micfun123/Mics-API-wrapper',
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        "Pillow==9.0.1"
    ]
)

# python3 setup.py bdist_wheel
# twine upload dist/*
# sudo rm -rf ./build ./dist ./*egg-info