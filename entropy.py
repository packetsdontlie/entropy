import io
import argparse
import os
import sys
import fnmatch

def main():
    """administrative args parsing"""
    
    parser = argparse.ArgumentParser(description='entropy', epilog="Exits with 0 on success")
    parser.add_argument('-p','--path', help='path to files', required=True)
    parser.add_argument('-f', '--filter', help='filter', required=False, type=str, default='txt')

    args = parser.parse_args()
    file_filter = '*.' + args.filter

    if args.path:
        for detect_file in locate_files(file_filter, args.path):
            score_it(detect_file)

def score_it(text_file_path):
    """reads a file, counts all terms and unique terms"""
    
    bag_of_words = []

    try: 
        with io.open(text_file_path, encoding='utf-8') as fh:
            for line in fh:
                unigrams = line.strip().split()
                bag_of_words.extend(unigrams)

            if bag_of_words:
                unique_terms = set(bag_of_words)
                unique_count = len(unique_terms)
                words_count = len(bag_of_words)
                entropy = float(unique_count)/float(words_count)

                verdict = "OK"
                if entropy > 0.85:
                    verdict = "ENTROPIC"
                if words_count < 500:
                    verdict = "TINY"
                if words_count > 35000:
                    verdict = "NOISY"

                print text_file_path, entropy, words_count, unique_count, verdict

    except UnicodeDecodeError:
            verdict = "ERR:DECODE"
            print text_file_path, verdict
    except IOError:
            verdict = "ERR:IO"
            print text_file_path, verdict


def locate_files(pattern, root):
    """descends into directories pulling out files, handsomely"""


    if os.path.exists(root):
        try:
            for path, dirs, files in os.walk(os.path.abspath(root)):
                for filename in fnmatch.filter(files, pattern):
                    yield os.path.join(path, filename)
        except:
            print "Could not traverse your -p (path)"
    else:
        print "Could not find your -p (path)"

if __name__ == "__main__":
    main()
