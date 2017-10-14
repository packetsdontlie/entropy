# entropy
A Python utility that calculates ratio between doc length and unique terms

## Usage

`python entropy.py -p /Users/someone -f '*'`

## Arguments

* -p / --path - the path to start descending (required)
* -f / --filter - the file extension to search for (optional, default is 'txt')

## Labels

* OK - file is considered normal
* ENTROPIC - unique terms are approaching total terms
* TINY - file has very few words
* NOISY - file has large number of words
* ERR:DECODE - could not open file, could be a UTF-8 error or a binary files
* ERR:IO - could not open file

## Output

* full name of file, entropy, word count, unique words, label

`/Users/someone/.cache/bower/packages/cc6d3adf8c2a36f7b163cc9479c3829c/3.10.1/lodash.min.js 0.855611150822 1399 1197 ENTROPIC`

