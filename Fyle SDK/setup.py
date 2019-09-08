import setuptools
from fylesdk import __version__

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='fylesdk',
    version=__version__,
    author='Meto Trajkovski',
    author_email='metot@hotmail.com',
    description='Python SDK for accessing Fyle APIs',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',  
    keywords=['fyle', 'api', 'python', 'sdk'],
    url='https://github.com/snarayanank2/fyle-sdk-py',
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)