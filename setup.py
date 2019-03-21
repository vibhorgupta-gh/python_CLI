from setuptools import setup

setup(
    name='kv',
    version='0.1',
    py_modules=['cli','server'],
    install_requires=[
        'Click',
        'Redis',
        'Flask',
    ],
    entry_points='''
        [console_scripts]
        store=cli:cli
    ''',
)