import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTestCommand(TestCommand):
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup( name ='Tame_Of_Thrones',
       version = '0.1',
       description='Geektrust Challenge - Tame Of Thrones',
       url='https://github.com/Lemniscite',
       author = 'Hiro',
       author_email='lemniscite@gmail.com',
       package_dir={'geektrust': 'src'},
       packages=['geektrust'],
       tests_require=['pytest'],
       cmdclass={'test': PyTestCommand},
       zip_safe=False
       )