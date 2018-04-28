import datetime
import sublime_plugin
class AddInfoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("insert_snippet",
        	{"contents":
        		"---\n"
        		"title: \n"
        		"date: " "%s"  %datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +"\n"
        		"tags: java 经验分享 \n"
        		"keywords: 维度 kylin 大数据 java java jar命令 彭双宝\n"
        		"categories: \n---"
        	}
        )



