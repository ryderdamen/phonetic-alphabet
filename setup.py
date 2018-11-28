import setuptools


def get_readme():
    with open('README.md') as f:
        return f.read()

INSTALL_REQUIRES = []
TESTS_REQUIRE = ['pytest']


setuptools.setup(
    name='phonetic_alphabet',
    version='0.1.0',
    description='Convert characters and digits to phonetic alphabet equivalents.',
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    keywords='phonetic alphabet aviation flight alpha bravo charlie niner',
    url='http://github.com/ryderdamen/phonetic-alphabet',
    author='Ryder Damen',
    author_email='dev@ryderdamen.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    test_suite='pytest',
    tests_require=TESTS_REQUIRE,
)