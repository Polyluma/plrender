
"""Setup for the plrender package."""

import setuptools

# with open('README.md') as f:
#     README = f.read()

setuptools.setup(
    author="Johannes Schacht",
    author_email="j@mono.io",
    name='plrender',
    license="No License",
    description='plrender is a python package for blender render.',
    version='v0.0.1',
    long_description='PLRENDER',
    url='https://github.com/Polyluma/plrender',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=[],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
    include_package_data=True,
    zip_safe=False
)