from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 3 - Alpha (Users should expect bugs and API changes)',
    'Intended Audience :: Licensed Users',
    'License :: Private License',
    'Programming Language :: Python :: 3'
]

setup(
    name='example',
    version='0.1.0',
    description='An example of a Python Library.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author='Stefan Rheeders',
    author_email='stefan.rheeders@gmail.com',
    license='private',
    classifiers=classifiers,
    keywords='example',
    packages=find_packages(),
    install_requires=[],
)