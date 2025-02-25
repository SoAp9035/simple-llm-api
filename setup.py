from setuptools import setup, find_packages


setup(
    name="simple-llm-api",
    version="1.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.3"
    ],
    author="Ahmet Burhan Kayalı",
    author_email="ahmetburhan1703@gmail.com",
    description="A simple and easy-to-use LLM API Wrapper",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SoAp9035/simple-llm-api",
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",

        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP",

        "License :: OSI Approved :: MIT License",
    ],
    keywords=["simple", "llm", "openai", "anthropic", "gemini", "mistral", "api", "wrapper"]
)