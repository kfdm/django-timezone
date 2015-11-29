from setuptools import find_packages, setup

from timezone import __version__, __homepage__

setup(
    name='django-timezone',
    description='Quick Timezone code',
    author='Paul Traylor',
    url=__homepage__,
    version=__version__,
    packages=find_packages(),
    install_requires=['pytz'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    entry_points={
        'powerplug.apps': ['timezone = timezone'],
    },
)
