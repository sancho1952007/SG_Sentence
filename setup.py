from setuptools import setup
setup_args=dict(
    name = "SG_Sentence",
    version = "1.0",
    author = "Sancho Godinho",
    description = "An Awesome Module to Encode & Decode A String...",
    long_description = "Please Visit: https://github.com/sancho1952007/SG_Sentence for All the Licence, Terms and Conditions How to Use, Etc...",
    packages = ["SG_Sentence"],
    keywords = ['sg_encode', 'sg_decode'],
    url = "https://github.com/sancho1952007/SG_Sentence",
    license_files = ('LICENSE'),
    project_urls = {
        "Bug Tracker": "https://github.com/sancho1952007/SG_Sentence/issues"
    }
)

install_requires = []

if __name__=='__main__':
    setup(**setup_args, install_requires=install_requires)