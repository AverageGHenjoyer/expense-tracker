from setuptools import setup, find_packages

setup(
    name="expense-tracker",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        'tabulate',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'expense-tracker =expense_tracker.main:main',
        ],
    },
)
