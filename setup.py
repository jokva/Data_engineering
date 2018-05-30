import setuptools

setuptools.setup(
    name = 'lpl',
    description = 'LAS3 parser and writer',
    packages = ['lpl'],
    platforms = 'any',
    install_requires = [
        'las >= 0.0.3',
        'pandas',
        'python-dateutil',
        'pytz',
        'six',
        'numpy >= 1.13',
    ],
    setup_requires = ['setuptools >= 28', 'pytest-runner'],
    tests_require = ['pytest'],
    entry_points = {
        'console_scripts': [
            'Corporate_WellDB_Log_Parser_Las=lpl.lpl:main'
        ],
    },
)
