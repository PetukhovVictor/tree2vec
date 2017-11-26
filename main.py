import sys

from pprint import pprint

from lib.Helpers.AstReader import AstReader
from lib.FeatureExtraction.FeatureExtractor import FeatureExtractor

if len(sys.argv) <= 1:
    sys.stderr.write('File with AST not specified.\n')
    exit()

ast_file = sys.argv[1]

root = AstReader.read(ast_file)

simple_features = [
    'depth',
    'depth_avg',
    'chars_length_avg',
    'chars_length_max'
]

features = [{
    'type': 'all_ngrams',
    'params': {
        'n': 3,
        'max_distance': 3
    }
}]

features.extend(map(lambda feature: {'type': feature}, simple_features))

features_extractor = FeatureExtractor(root, features)
features = features_extractor.extract()

pprint(features)
