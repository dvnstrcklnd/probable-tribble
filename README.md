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