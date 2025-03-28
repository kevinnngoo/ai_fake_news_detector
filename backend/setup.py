from setuptools import setup, find_packages

setup(
    name="ai_fake_news_detector",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-jwt-extended',
        'pymongo',
        'python-dotenv',
    ],
)