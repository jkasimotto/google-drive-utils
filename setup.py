from setuptools import setup, find_packages

setup(
    name='google-drive-api-utils',
    version='0.1.0',
    description='A collection of utilities for working with the Google Drive API',
    author='Julian Otto',
    author_email='julianotto@outlook.com',
    url='https://github.com/jkasimotto/google-drive-api-utils',
    packages=find_packages(),
    install_requires=[
        'google-auth',
        'google-api-python-client',
        'tqdm',
        'PyYAML',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
