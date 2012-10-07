import sublime, sublime_plugin
from titlecase import titlecase

class SmartTitleCaseCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if region.empty():
				region = self.view.line(region)

			s = self.view.substr(region)
			s = titlecase(s)
			self.view.replace(edit, region, s)
