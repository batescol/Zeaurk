from abc import ABCMeta, abstractmethod

# Changed update to either look (for observer) or 
# show (for observable) to allow double inheritance
class Observer(object):
	__metaclass__ = ABCMeta

	@abstractmethod
	def look(self, obj):
		pass

# Slightly modified observer pattern, simplified because
# Our program will never have more than one observer per
# observable
class Observable(object):
	def __init__(self):
		self.obser = None

	def setObser(self, obser):
		if self.obser is not None:
			raise RuntimeError("Error: " + self + " is already being observed by " + self.obser)
		self.obser = obser

	def resetObser(self, obser):
		if self.obser is None:
			raise RuntimeError("Error: " + self + " is not being observed")
		self.obser = None

	def show(self):
		if self.obser is None:
			raise RuntimeError("Error: " + self + " is not being observed")
		self.obser.look(self)