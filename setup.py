# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst', 'r') as fp:
    long_description = fp.read()

with open('requirements.txt', 'r') as fp:
    requirements = fp.read().splitlines()

with open('requirements-extras.txt', 'r') as fp:
    requirements_extras = fp.read().splitlines()

setup(
    name='mocp',
    version='0.4.10',
    description='A Python library to control the MOC (music on console) audio player',
    long_description=long_description,
    author='Ken',
    author_email='kenjyco@gmail.com',
    license='MIT',
    url='https://github.com/kenjyco/mocp',
    download_url='https://github.com/kenjyco/mocp/tarball/v0.4.10',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    extras_require={
        'extras': requirements_extras,
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Sound/Audio :: Players',
        'Topic :: Software Development :: Libraries',
    ],
    keywords=['moc', 'mocp', 'cli', 'command-line', 'console audio', 'mp3 player', 'kenjyco']
)
