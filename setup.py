import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ig_profile",
    version="1.0",
    author="Debdut Goswami",
    author_email="debdutgoswami@gmail.com",
    description="A simple package to extract the profile picture of a instagram user.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/debdutgoswami/instagram-profile-picture",
    download_url = 'https://github.com/debdutgoswami/instagram-profile-picture/archive/v1.0.tar.gz',
    keywords = ['INSTAGRAM', 'PROFILE', 'PICTURE'],
    packages=setuptools.find_packages(),
    install_requires=[
        'beautifulsoup4',
        'Pillow'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)