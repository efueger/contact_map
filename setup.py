"""
setup.py for contact_map
"""
from setuptools import setup
import os
import subprocess

##########################
VERSION = "0.1.3"
ISRELEASED = False
if not ISRELEASED:
    VERSION += ".dev"
__version__ = VERSION
PACKAGE_VERSION = VERSION
REQUIREMENTS=['future', 'numpy', 'mdtraj', 'scipy', 'pandas']
##########################

DESCRIPTION="""
Contact maps based on MDTraj; useful for studying for intramolecular and
intermolecular contacts from simulations of biomolecular systems. For a
more detailed description, see package's documentation.
"""
if os.path.isfile('README.rst'):
    DESCRIPTION = open('README.rst').read()

################################################################################
# Writing version control information to the module
################################################################################

def git_version():
    # Return the git revision as a string
    # copied from numpy setup.py
    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = 'Unknown'

    return GIT_REVISION


def write_version_py(filename='contact_map/version.py'):
    cnt = """
# This file is automatically generated by setup.py
short_version = '%(version)s'
version = '%(version)s'
full_version = '%(full_version)s'
git_revision = '%(git_revision)s'
release = %(isrelease)s

if not release:
    version = full_version
"""
    # Adding the git rev number needs to be done inside write_version_py(),
    # otherwise the import of numpy.version messes up the build under Python 3.
    FULLVERSION = VERSION
    if os.path.exists('.git'):
        GIT_REVISION = git_version()
    else:
        GIT_REVISION = 'Unknown'

    if not ISRELEASED:
        FULLVERSION += '-' + GIT_REVISION[:7]

    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION,
                       'full_version': FULLVERSION,
                       'git_revision': GIT_REVISION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()

################################################################################
# Installation
################################################################################

write_version_py()

setup(
    name="contact_map",
    author="David W.H. Swenson",
    author_email="dwhs@hyperblazer.net",
    version=PACKAGE_VERSION,
    license="LGPL",
    url="http://github.com/dwhswenson/contact_map",
    packages=['contact_map', 'contact_map.tests'],
    package_dir= {
        'contact_map': 'contact_map',
        'contact_map.tests': 'contact_map/tests'
    },
    package_data={'contact_map': ['tests/*pdb']},
    ext_modules=[],
    scripts=[],
    description="Contact maps based on MDTraj",
    long_description=DESCRIPTION,
    platforms=['Linux', 'Mac OS X', 'Unix', 'Windows'],
    install_requires=REQUIREMENTS,
    requires=REQUIREMENTS,
    tests_require=["pytest", "pytest-cov", "python-coveralls"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry'
    ]
)


