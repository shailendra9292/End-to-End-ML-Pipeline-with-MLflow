from setuptools import setup, find_packages

def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()

    if "-e ." in requirements:
        requirements.remove("-e .")
    return requirements

REPO_NAME = "End-to-End-ML-Pipeline-with-MLflow"
AUTHOR = "Shailendra Singh"
AUTHOR_EMAIL = "shailendra24.singh@gmail.com"
SRC_REPO = "mlProject"
__version__ = "0.0.0"

setup(name='mlProject', 
    version=__version__, 
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description='Complete ML Pipeline',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR}/{REPO_NAME}',
    project_urls={
    "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires= get_requirements()
      )