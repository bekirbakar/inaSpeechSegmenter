#  Load the API
import sys

from inaSpeechSegmenter import Segmenter
from inaSpeechSegmenter.export_funcs import seg2csv, seg2textgrid

# select a media to analyse
#  any media supported by ffmpeg may be used (video, audio, urls)
media = sys.argv[1]

# create an instance of speech segmenter
# this loads neural networks and may last few seconds
#  Warnings have no incidence on the results
seg = Segmenter()

# segmentation is performed using the __call__ method of the segmenter instance
segmentation = seg(media)

#  the result is a list of tuples
# each tuple contains:
# * label in 'male', 'female', 'music', 'noEnergy'
# * start time of the segment
#  * end time of the segment
print(segmentation)

# this writes the resulting segmentation into a csvfile
# the csv file may be used to import segmentation into visualization softwares,
#  such as sonic-visualiser: https://www.sonicvisualiser.org
seg2csv(segmentation, 'myseg.csv')


# export to praat TextGrid is also supported
seg2textgrid(segmentation, 'myseg.TextGrid')

print('Done, check myseg.csv and myseg.TextGrid files.')
