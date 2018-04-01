from setuptools import setup, find_packages

setup(
    name='cexapi',
    version='0.0.1',
    description='A python CEX WeBuy Wrapper',
    url='https://github.com/hiddencipher/CEX-API',
    author='HiddenCipher',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['requests'],
)
