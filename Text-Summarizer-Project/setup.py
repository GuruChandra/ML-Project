import setuptools

with open('ReadMe.md','r',encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "ML-Project"
AUTOR_USER_NAME = "GuruChandra"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "guruchandu4@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package fro NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTOR_USER_NAME}/{REPO_NAME}",
    project_url ={
        "Bug Tracker": f"https://github.com/{AUTOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
