import setuptools

setuptools.setup(
    name="firebase-comm",
    version="0.0.001",
    author="<author>",
    author_email="coder.henkelmann@gmail.com",
    description="A boilerplate to communicate with firebase",
    packages=setuptools.find_packages(include=["src"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)