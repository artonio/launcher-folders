#!/usr/bin/python
class ShortcutItem(object):
	_appName = ""
	_appIcon = ""
	_execPath = ""
	_iconSize = 48
	_fontSize = 11
	_itemWidth = 48

	@property
	def appName(self):
		return self._appName
	@appName.setter
	def appName(self, appName):
		self._appName = appName

	@property
	def appIcon(self):
		return self._appIcon
	@appIcon.setter
	def appIcon(self, appIcon):
		self._appIcon = appIcon

	@property
	def execPath(self):
		return self._execPath
	@execPath.setter
	def execPath(self, execPath):
		self._execPath = execPath

	@property
	def iconSize(self):
		return self._iconSize
	@iconSize.setter
	def iconSize(self, iconSize):
		self._iconSize = iconSize	

	@property
	def fontSize(self):
		return self._fontSize
	@fontSize.setter
	def fontSize(self, fontSize):
		self._fontSize = fontSize

