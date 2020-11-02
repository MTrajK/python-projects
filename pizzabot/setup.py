from setuptools import setup, find_packages

setup(
    name='pizzabot',
    version='0.0.1',
    description='Pizzabot instructions.',
    python_requires='>=3.9',
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pizzabot=pizzabot.cli:run'
        ]
    }
)