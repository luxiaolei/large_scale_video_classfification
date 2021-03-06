"""
dataset class
"""

import tensorflow as tf
import os

tf.app.flags.DEFINE_string('train_directory', '/tmp/UCF101/TFRecords/train/', 
						'output TFRecords training data directory')
tf.app.flags.DEFINE_string('valid_directory', '/tmp/UCF101/TFRecords/valid/', 
						'output TFRecords validation data directory')
tf.app.flags.DEFINE_string('test_directory', '/tmp/UCF101/TFRecords/test/', 
						'output TFRecords training data directory')

FLAGS = tf.app.flags.FLAGS

class Dataset:
	def __init__(self, used_for='train'):
		self.used_for = used_for
		self.filenames = self._filenames()
		self.reader = tf.TFRecordReader()


	def _filenames(self):
		if self.used_for == 'train':
			return [os.path.join(
				FLAGS.train_directory, fn) for fn in os.listdir(FLAGS.train_directory)]
		elif self.used_for == 'valid':
			return [os.path.join(
				FLAGS.valid_directory, fn) for fn in os.listdir(FLAGS.valid_directory)]
		else:
			return [os.path.join(
				FLAGS.test_directory, fn) for fn in os.listdir(FLAGS.test_directory)]
