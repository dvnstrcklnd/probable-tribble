# Probable Tribble
Tools for processing lists and strings

## Installation
Probable Tribble is designed to be run in a [Docker](https://www.docker.com/get-started)
container. Please install Docker if you don't already have it.

To install the app:
```bash
git clone https://github.com/dvnstrcklnd/probable-tribble.git
cd probable-tribble
docker build -t probable-tribble .
```

## Usage
To count the number of integers above and below a threshold:
```bash
docker run probable-tribble count-above-below -l 1 2 3 -v 2
> above: 1, below: 1.
```
To rotate a string by removing n characters from the end and placing them at the beginning:
```bash
docker run probable-tribble rotate-string -s Round -n 2
> ndRou
```

## What I would change about my favorite language
For most purposes, there are two reasons to choose a programming language: its suitability for 
the task at hand, and the readability of the resulting code. I prefer to write and read code in 
Ruby, because I find the syntax to be the most readable. One aspect of Ruby that greatly contributes
to readabiliy is the large number of clearly named built-in methods for most object types. For example, 
`my_array.flatten` is vastly easier to read than the Python equivalent 
([whatever that is](https://stackabuse.com/python-how-to-flatten-list-of-lists/)). 

Not coincidentally, the large number of built-in methods makes Ruby well-suited for a wide range of tasks. Nevertheless, 
languages are also measured by the availability of high-quality libraries that are available. A major weakness
of Ruby, as compared to Python is the relative lack of data science tooling. If I could change one thing about Ruby, 
it would be to make libraries such as Pandas and SciKit available.
