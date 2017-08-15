# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2017-08-15 14:58:28
# @Last Modified by:   boyac
# @Last Modified time: 2017-08-15 15:22:52

from Base import *

class InClass(BaseClass):
	def __init__(self):
		super(InClass, self).__init__()
		self.x = 17

class InClass2(BaseClass):
	def __init__(self):
		super(InClass2, self).__init__()
	def printHam(self):
		print "Ham2"

class InClass3(InClass, InClass2):
	def __init__(self):
		super(InClass3, self).__init__()
		print self.x
		self.printHam()

i = InClass3()
