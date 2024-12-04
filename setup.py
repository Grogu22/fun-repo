from setuptools import setup, find_packages

setup(
    name='fun-repo',  # Name of your repository or package
    version='0.1.0',        # Version number
    packages=['text-generator'],   # List the specific module(s) you want to install
    install_requires=[],    # Any external dependencies
    description='A collection of Python modules',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Grogu22',
    author_email='grogu22@example.com',
    url='https://github.com/Grogu22/fun-repo',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
