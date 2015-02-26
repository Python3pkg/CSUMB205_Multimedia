from setuptools import setup
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='csumb205_multimedia',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='0.8.8',

    description='A easier-to-use, academic wrapper class for different multimedia',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/pwalker91/CSUMB205_Multimedia',

    # Author details
    author='Peter Walker',
    author_email='pwalker@csumb.edu',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Education',
        'Topic :: Artistic Software',
        'Topic :: Education',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',

        #The language this project is written in
        'Natural Language :: English',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        #'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',

        # Specify the operating systems that this module should work on
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows :: Windows 7'
    ],

    # What does your project relate to?
    keywords='image multimedia manipulation education csumb 205',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    py_modules=['simpleAudio',
                'simpleImage',
                'simpleVideo'],

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['Pillow', 'numpy'], #'moviepy', ...],
)
