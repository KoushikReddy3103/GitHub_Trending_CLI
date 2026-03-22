from setuptools import setup, find_packages

setup(
    name="trending-repos",
    version="1.0.0",
    # project layout places the package sources under the `trending_repos/` directory
    packages=find_packages(where="trending_repos"),
    package_dir={"": "trending_repos"},
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "trending-repos=trending_repos.cli:main"
        ]
    },
)