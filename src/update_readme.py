import json
import os
import git

def is_git_repo(path):
    try:
        _ = git.Repo(path)
        return True
    except git.exc.InvalidGitRepositoryError:
        return False

def load_head(file):
	with open("../res/head.md", 'r') as f:
		for line in f:
			file.write(line)

def load_content(file):
	file.write("## Contents\n")
	file.write("- [Open Source Libraries](#open-source-libraries)\n")
	file.write("- [Papers](#papers)\n")

	path = '../res/papers'

	for pf in sorted(os.listdir(path)):
		if not pf.endswith(".json"):
			continue
		with open(os.path.join(path, pf), 'r') as f:
			title = json.load(f)['title']
			file.write("  - [{}](#{})\n".format(title, title.lower().replace(' ', '-')))

	file.write("- [Contribute](#contribute)\n")

def load_lib(file):
	file.write("## Open Source Libraries\n")
	with open("../res/library.json", 'r') as f:
		libraries = json.load(f)
	for lib in libraries:
		name = lib['name']
		source = lib['source']
		repo = source.split('github.com/', 1)[1]
		file.write("- [{}]({}) ![GitHub stars](https://img.shields.io/github/stars/{}.svg?logo=github&label=Stars)\n".format(name, source, repo))

def load_paper(file):
	file.write("## Papers\n")

	with open('../.github/citation/citation.json', 'r') as f:
		citation = json.load(f)

	path = '../res/papers'
	for pf in sorted(os.listdir(path)):
		if not pf.endswith(".json"):
			continue
		with open(os.path.join(path, pf), 'r') as f:
			table = json.load(f)
			title = table['title']
			file.write("### {}\n".format(title))
			file.write("| Venue | Title | Affiliation | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Link&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;Source&nbsp;&nbsp; |\n")
			file.write("| :---: | :---: | :---------: | :---: | :----: |\n")
			for paper in table['paper']:
				file.write("|{}|".format(paper['venue']))
				file.write("{}|".format(paper['name']))
				file.write("{}|".format(paper['affiliation']))
				if 'link' in paper:
					file.write(" [[paper]]({})".format(paper['link']))
					cite = citation[paper['name']]['citation']
					if cite > 10000:
						cite = int(cite / 1000 + 0.5)
						cite = '{}k'.format(cite)
					elif cite > 1000:
						cite = int(cite / 100 + 0.5) / 10
						cite = '{}k'.format(cite)
					file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
				file.write("|")
				if 'source' in paper:
					source = paper['source']
					file.write(" [[code]]({})".format(source))
					repo = source.split('github.com/', 1)[1]
					if repo.count('/') == 1:
						file.write("![GitHub stars](https://img.shields.io/github/stars/{}.svg?logo=github&label=Stars)".format(repo))

				file.write("|\n")

				'''
				file.write("- [**{}**]".format(paper['venue']))
				file.write(" {}".format(paper['name']))
				file.write(" (*{}*)".format(paper['affiliation']))
				if 'link' in paper:
					file.write(" [[paper]]({})".format(paper['link']))
					cite = citation[paper['name']]['citation']
					file.write("![Scholar citations](https://img.shields.io/badge/Citations-{}-_.svg?logo=google-scholar&labelColor=4f4f4f&color=3388ee)".format(cite))
				if 'source' in paper:
					source = paper['source']
					file.write(" [[code]]({})".format(source))
					repo = source.split('github.com/', 1)[1]
					if repo.count('/') == 1:
						file.write("![GitHub stars](https://img.shields.io/github/stars/{}.svg?logo=github&label=Stars)".format(repo))

				file.write("\n")
				'''


file = open("../README.md", 'w')

load_head(file)
load_content(file)
load_lib(file)
load_paper(file)

file.close()