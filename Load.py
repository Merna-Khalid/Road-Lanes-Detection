#python version 3.5

import cv2
import numpy as np
from enum import Enum
from pathlib import Path


class DatasetType(Enum):
	TRAINING = 0
	VALIDATION = 1
	TESTING = 2

	@classmethod
	def default(cls):
		return DatasetType.TRAINING


# general dataset for images
class Dataset:

	def __init__(self, path, setType):
		self.path = path
		self.setType = setType

	# reads images in the folder only
	# no subdirectories 
	# path : pathlib.path
	# dFormat : str
	def readImagesInDir(self, path, dFormat='jpg'):
		files = list(path.glob('*.' + dFormat))
		images = np.array()
		for f in files:
			images.append( ( f.parts[-1], cv2.imread(str(f)) ) )
		return images

	#reads images in subdirs
	# folder : str
	# dFormat : str
	def readImagesInSub(self, folder, dFormat='jpg'):
		path = Path(folder)
		images = np.array()
		images.append( ( f.parts[-1], self.readImagesInDir(path, dFormat) ) )
		for f in path.iterdir():
			if f.is_dir():
				images.append(self.readImagesInDir(f, dFormat))
		return images.flatten()

	# annotation 
	def readAnnotationInDir(self, path):
		files = list(path.glob('*.txt'))
		annotations = np.array()
		for f in files:
			string = f.read_text()
			annotations.append( ( f.parts[-1], np.array([int(s) for s in example_string.split(',')]) ) )
		return annotations

	def readImagesInSub(self, folder):
		path = Path(folder)
		annotations = np.array()
		annotations.append( ( f.parts[-1], self.readAnnotationInDir(path) ) )
		for f in path.iterdir():
			if f.is_dir():
				annotations.append(self.readAnnotationInDir(f))
		return annotations.flatten()


	def load():
		self.images = np.array()
