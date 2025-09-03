from music21 import converter

score = converter.parse('path_to_score.xml')
print(score.analyze('key'))
