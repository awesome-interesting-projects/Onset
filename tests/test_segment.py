import sys
import os.path as path

base_directory = path.dirname(path.dirname(path.abspath(__file__)))

sys.path.append(path.join(base_directory, 'app'))

from segment import Segment


def test_initialisation():
    feature_dictionary = {'stress': '+', 'long': '-', 'continuant': '0',
                          'IPA': 'b'}

    segment = Segment.from_dictionary(feature_dictionary)

    assert segment.positive == ['stress']
    assert segment.negative == ['long']


def test_setters():
    feature_dictionary = {'stress': '+', 'long': '-', 'continuant': '0',
                          'IPA': 'b'}

    segment = Segment.from_dictionary(feature_dictionary)

    segment.positive = 'long'
    assert segment.positive == ['stress', 'long']
    assert segment.negative == []

    segment.negative = 'stress'
    assert segment.positive == ['long']
    assert segment.negative == ['stress']

    segment.negative = 'stress'
    assert segment.positive == ['long']
    assert segment.negative == ['stress']
