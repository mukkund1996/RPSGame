from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='rpsgame',
    version='1.1',
    description='Classic game of Rock Paper and Scissors',
    project_description="It is exactly what you think it is.",
    url='https://github.com/mukkund1996/RPSGame',
    author='Mukkund Sunjii',
    author_email='mukkundsunjii@gmail.com',
    license='MIT',
    packages=['rpsgame'],
    entry_points={
        'console_scripts': ['rpsgame=rpsgame.main:__main__'],
    },
    install_requires=[
        "emoji",
    ],
    zip_safe=False
)