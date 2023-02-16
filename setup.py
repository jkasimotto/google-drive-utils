from setuptools import setup, find_packages

setup(
    name='google_drive_utils',
    version='0.1.0',
    description='A collection of utilities for working with the Google Drive API',
    author='Julian Otto',
    author_email='julianotto@outlook.com',
    url='https://github.com/jkasimotto/google_drive_utils',
    packages=find_packages(),
    install_requires=[
        'google-auth',
        'google-api-python-client',
        'tqdm',
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'download-drive-files=google_drive_utils.cli.download:main',
            'count-drive-files=google_drive_utils.cli.count:main',
        ]
    }
)
