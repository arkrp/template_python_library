from setuptools import setup, find_packages

setup(name="{{ cookiecutter.project_slug }}",
    version="0.1",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            'example_command={{ cookiecutter.project_slug }}.{{ cookiecutter.project_slug }}:example_command',
            ]
    }
)
