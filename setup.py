from setuptools import setup, find_packages

setup(
    name='rl-shaper-toolkit',
    version='0.1.0',
    author='Dhrumi Shah',
    author_email='dhrumishah3695@gmail.com',
    description='A toolkit for implementing reward shaping techniques in reinforcement learning.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DhrumiS04/rl-shaper-toolkit',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)