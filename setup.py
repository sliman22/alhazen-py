from setuptools import setup, find_packages

setup(
    name='alhazen-py',
    description='Command-line interface for alhazen-py',
    packages=find_packages(),
    install_requires=[
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'alhazen = alhazen.cli:main',
        ],
    },
)