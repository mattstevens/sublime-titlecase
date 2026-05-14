import sublime_plugin

try:
    from .titlecase import titlecase
except ValueError:
    from titlecase import titlecase


class SmartTitleCaseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():

                line = self.view.line(region)
                lineStr = self.view.substr(line)

                relIndex = region.begin() - line.begin()

                end = lineStr.find("}", relIndex)
                sta = lineStr[::-1].find("{", len(lineStr) - relIndex)

                if sta is not -1 and end is not -1:
                    region = sublime.Region(line.begin() + (len(lineStr) - sta), line.begin() + end)

                else:
                    region = self.view.line(region)

            s = self.view.substr(region)
            s = titlecase(s)
            self.view.replace(edit, region, s)
