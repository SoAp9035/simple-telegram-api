from setuptools import setup, find_packages


setup(
    name="simple-telegram-api",
    version="0.9.0",
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author="Ahmet Burhan Kayalı",
    author_email="ahmetburhan1703@gmail.com",
    description="A simple and easy-to-use Python wrapper for Telegram bots",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SoAp9035/simple-telegram-api",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",

        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",

        "License :: OSI Approved :: MIT License",
    ],
    keywords=["simple", "telegram", "bot", "api", "wrapper"]
)
