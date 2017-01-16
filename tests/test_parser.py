import sys
import csv
import os.path as path

base_directory = path.dirname(path.dirname(path.abspath(__file__)))

sys.path.append(path.join(base_directory, 'app'))

from parse import tokenise, valid_subword, token_to_segment

# Load data
with open(path.join(base_directory, 'app', 'data', 'features.csv'), 'r') as f:
    segments = [segment for segment in csv.DictReader(f)]

with open(path.join(base_directory, 'app', 'data', 'diacritics.csv'), 'r') as f:
    diacritics = [segment for segment in csv.DictReader(f)]

available_segments = [segment['IPA'] for segment in segments]
available_diacritics = [segment['IPA'] for segment in diacritics]


def test_tokenise():
    assert tokenise('bok͡piʰ', available_segments, available_diacritics) == ['b', 'o', 'k͡p', 'iʰ']
    assert tokenise('', available_segments, available_diacritics) == []


def test_valid_subword():
    assert valid_subword('b', available_segments, available_diacritics)
    assert valid_subword('bʰ', available_segments, available_diacritics)
    assert valid_subword('bʰ\u0330', available_segments, available_diacritics)
    assert valid_subword('k̟͡x̟', available_segments, available_diacritics)

    assert not valid_subword('ʰ', available_segments, available_diacritics)
    assert not valid_subword('', available_segments, available_diacritics)


def test_token_to_segment():
    segment = token_to_segment('b', segments, diacritics)

    assert segment.positive == ['consonantal', 'voice', 'labial']
    assert segment.negative == ['syllabic', 'stress', 'long', 'sonorant', 'continuant', 'delayedrelease', 'approximant', 'tap', 'trill', 'nasal', 'spreadglottis', 'constrictedglottis', 'round', 'labiodental', 'coronal', 'lateral', 'dorsal']

    segment = token_to_segment('bʰː', segments, diacritics)

    assert segment.positive == ['consonantal', 'voice', 'labial', 'spreadglottis', 'long']
    assert segment.negative == ['syllabic', 'stress', 'sonorant', 'continuant', 'delayedrelease', 'approximant', 'tap', 'trill', 'nasal', 'constrictedglottis', 'round', 'labiodental', 'coronal', 'lateral', 'dorsal']