from setuptools import setup, find_packages
from os import path
import re
import subprocess


here = path.abspath(path.dirname(__file__))


def get_version():
    try:
        label = subprocess.check_output(
            ["git", "describe", "--tags"], universal_newlines=True
        ).strip()
    except subprocess.CalledProcessError:
        return "0.0.0"
    version = re.search(r"[0-9]\.[0-9]\.[0-9]", label)
    if not version:
        return "0.0.0"
    return version.group(0)


# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="django-domain-specific-language",
    version=get_version(),
    description="DSL for Django",
    long_description=long_description,
    url="https://github.com/treussart/django-dsl",
    author="Treussart Matthieu",
    author_email="matthieu@treussart.com",
    # Choose your license
    license="GPLv3",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 5 - Production/Stable",
        # 'Environment :: Console',
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Framework :: Django :: 3.0",
        "Topic :: Software Development :: Interpreters",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3 :: Only",
    ],
    # What does your project relate to?
    keywords="django dsl domain-specific-language",
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    # packages=find_packages(exclude=['docs', 'tests', '.venv', '.idea', 'htmlcov']),
    # packages=['TransilienDomoticz'],
    packages=find_packages(),
    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    # py_modules=["transilien"],
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=['peppercorn'],
    include_package_data=True,
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'transilien = Transilien_Domoticz.transilien:transilien',
    #     ],
    # },
    install_requires=["Django>=3", "ply>=3"],
)
