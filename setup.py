from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='fear-and-greed-crypto',
    version='0.1.0',
    description='A simple wrapper for the Alternative.me Crypto Fear and Greed Index API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Rhett Reisman',
    author_email='rhett@rhett.blog',
    license='MIT',
    url='https://github.com/rhettre/fear-and-greed-crypto',
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    keywords=['bitcoin', 'crypto', 'fear-and-greed-index', 'trading', 'finance', 
              'cryptocurrency', 'market-sentiment', 'alternative-me', 'bitcoin-trading',
              'crypto-trading', 'market-analysis', 'trading-signals', 'api-wrapper',
              'technical-analysis', 'market-indicators', 'crypto-sentiment',
              'bitcoin-sentiment', 'market-psychology', 'trading-psychology'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.9',
)