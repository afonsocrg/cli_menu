from setuptools import setup, find_packages

setup(
    name='cli_menu',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    python_requires='>=3.6',

    # Metadata
    author='afonsocrg',
    author_email='afonso.crg@gmail.com',
    description='A library for creating interactive CLI menus in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/afonsocrg/cli_menu',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='cli, menu, terminal, console',
)
