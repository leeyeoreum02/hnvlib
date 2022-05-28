import re
from setuptools import setup, find_packages


def get_version():
    with open('yolox/__init__.py', 'r') as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(), re.MULTILINE
        ).group(1)
    return version


def get_install_requirements():
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        reqs = [x.strip() for x in f.read().splitlines()]
    reqs = [x for x in reqs if not x.startswith('#')]
    return reqs


def get_long_description():
    with open('README.rst', encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    name='hnvcode',
    version=get_version(),
    description='Standard code library for HnV Lab.',
    author='Summer Lee',
    maintainer='Summer Lee',
    maintainer_email='leeyeoreum01@gmail.com',
    url='https://github.com/leeyeoreum02/hnvlib',
    # license='BSD',
    packages=find_packages(),
    # Sympy 1.4 is needed for printing tests to pass, but 1.3 will still work
    install_requires=get_install_requirements(),
    python_requires='<3.10',
    long_description=get_long_description(),
    classifiers=[
        # 'Development Status :: 4 - Beta',
        # 'Environment :: Console',
        # 'Intended Audience :: Science/Research',
        # 'License :: OSI Approved :: BSD License',
        'Natural Language :: Korean',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        # 'Topic :: Scientific/Engineering :: Mathematics',
        # 'Topic :: Scientific/Engineering :: Physics',
    ],
    project_urls={
        'Documentation': 'https://hnvlib.readthedocs.io',
        # 'Bug Tracker': 'https://github.com/leeyeoreum02/standard-code/issues',
        'Source Code': 'https://github.com/leeyeoreum02/hnvlib',
    },
)