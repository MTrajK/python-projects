from setuptools import setup, find_packages

setup(
    name='boilerplate',
    version='0.0.1',
    description='Python project boilerplate.',
    author='Meto Trajkovski',
    python_requires='>=3',
    install_requires=[],
    # If you have only one package then use: packages=['boilerplate']
    packages=find_packages(exclude=('tests')),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'boilerplate=boilerplate.main:M'
        ]
    }
)