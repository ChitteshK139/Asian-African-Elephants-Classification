import setuptools

with open("README.md","r",encoding="utf-8") as f1:
    long_description=f1.read()

__version__="0.0.0"

REPO_NAME='Asian_African_Elephants_Classification'
AUTHOR_USER_NAME="Chittesh139"
SRC_REPO="Asian_African_Elephants_Classification"
AUTHOR_EMAIL="chitteshkumar13@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
)