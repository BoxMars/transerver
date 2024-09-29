from setuptools import setup, find_packages

setup(
    name='transerver',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        # 'requests',  
        'flask',
        'toml',
        'argparse',
        'transformers',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'transerver=transerver.main:main',  
        ],
    },
    author='Box, Huakang Zhang',
    author_email='me@boxz.dev',
    description='A server for interacting LLM model locally with OpenAI style API using transformers',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/boxmars/transerver',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)