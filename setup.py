import setuptools


long_description = "My long description"

setuptools.setup(
    name="Casino-Project",
    version="0.0.1",
    author="Dauirzhan Akmurat",
    author_email="s25674@pjwstk.edu.pl",
    description="Casino Project",
    long_description = long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/shkroba/nonion",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "nonion==0.4.4",
    ],
)