from setuptools import setup, find_packages

setup(
    name="coderoast",
    version="0.2.0",
    packages=find_packages(),
    description="A library that insults programmers when their code throws errors",
    long_description="""
        CodeRoast is a silly Python library that catches exceptions and provides
        insulting commentary on your programming skills. Great for masochistic
        programmers or teaching humility to overconfident coders.
    """,
    author="Not a Real Programmer",
    author_email="notarealprogrammer010@gmail.com",
    url="https://github.com/notarealprogrammer001/coderoast",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Debuggers",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
)