import sublime
import sublime_plugin


class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.run_command("insert_snippet",
            {
                "contents": "/**""\n"
                " * @Author:      name""\n"
                " * @DateTime:    "  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
                " * @Description: Description""\n"
                " */"
            }
