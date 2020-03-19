import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ig-profile", # Replace with your own username
    version="0.0.1",
    author="Debdut Goswami",
    author_email="debdutgoswami@gmail.com",
    description="A simple package to extract the profile picture of a instagram user.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debdutgoswami/instagram-profile-picture",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)