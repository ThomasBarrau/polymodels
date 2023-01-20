from setuptools import setup, find_packages

from polymodels.version import __version__

setup(
    name='polymodels',
    version=__version__,
    description='Estimating polymodels and derive indicators',
    long_description=(
        'Estimation of polymodels using various methodologies, for full sample and rolling '
        'regressions. Computation of various indicators of goodness of fit, concavity, '
        'drawdowns prediction, etc.'),
    url='https://www.linkedin.com/in/thomas-barrau',
    author='Thomas Barrau',
    author_email='thomas@barrau.eu',
    packages=find_packages(exclude=["tests"]),
    python_requires='>=3.8',
    extras_require={
        'test': [
            'pylint',
            'pytest',
            'black',
        ],
    },
    install_requires=[
        'pandas',
        'numpy',
    ],
)
