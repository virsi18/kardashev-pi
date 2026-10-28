from setuptools import setup, find_packages

setup(
    name="kardashev-pi",
    version="1.0.0",
    description="Relativistic Spacetime Consensus & Thermodynamic GCV Settlement Engine (1 Pi = 314,159 TEU)",
    author="Kardashev-Pi Working Group",
    author_email="pioneers@kardashev-pi.io",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "kardashev-pi=kardashev_pi.cli.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
