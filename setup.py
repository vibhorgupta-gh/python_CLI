from setuptools import setup

setup(
    name='kv',
    version='0.1',
    py_modules=['app'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        store=app:main
    ''',
)