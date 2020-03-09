import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="getsitemap-hsiafongw", 
    version="0.0.1",
    author="Hsiaofong Wayne",
    author_email="hsiaofong.w@gmail.com",
    description="A small and simple package crawl urls from a website sitemap",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hsiaofongw/getsitemap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)