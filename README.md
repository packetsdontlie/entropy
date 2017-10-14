# entropy
A Python utility that calculates ratio between doc length and unique terms

## Usage

`python entropy.py -p /Users/b -f '*'`

## Arguments

-p / --path - the path to start descending (required)
-f / --filter - the file extension to search for (optional, default is 'txt')

## Outputs

* OK - file is considered normal
* ENTROPIC - unique terms are approaching total terms
* TINY - file has very few words
* NOISY - file has large number of words
* ERR:DECODE - could not open file, could be a UTF-8 error or a binary files
* ERR:IO - could not open file
