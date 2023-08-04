from setuptools import setup, find_packages
from pathlib import Path
base_path = Path(__file__).parent
long_description = (base_path / "README.md").read_text()


setup(
    name='sdxl', 
    version='1.0.0',  
    author='Koushik',
    license="MIT",
    author_email='koushikk@outlook.com',
    description='Reverse engineered API of Stable Diffusion XL 1.0 ( Midjourney Alternative ), A text-to-image generative AI model that creates beautiful 1024x1024 images.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/KoushikNavuluri/stable-diffusion-xl-api/', 
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
    package_dir={
    "": "sdxl"
    },
    py_modules=["sdxl"],
    keywords=['stable diffusion', 'ai', 'midjourney', 'API', 'requests', 'images' ,'llm' ,'sdxl' , 'replicate'],
    install_requires=[
        'requests'  
    ],
    python_requires=">=3.7",
)
