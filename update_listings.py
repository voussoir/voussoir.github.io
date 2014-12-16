import json
import os
TEMPLATE_AUDIO = """
		<div class="audioelement">
			<a href="{f}">{f}</a>
			<audio controls
			  src="{f}">
			Your user agent does not support the HTML5 Audio element.
			</audio>
		</div>
		"""
TEMPLATE_IMAGE = """
		<div class="imagelinkelement">
			<a href="{f}">{f}</a>
		</div>
		"""
TEMPLATE_ZIP = """
		<div class="ziplinkelement">
			<a href="{f}">{f}</a>
		</div>
		"""
SPLITTER = "<!-- Automatic -->"

def listing(directory, htmlfilename, template):
	files = os.listdir(directory)
	files.remove('index.html')
	files.sort()
	divs = []
	for f in files:
		divs.append(template.format(f=f))
	page = open(htmlfilename, 'r')
	html = page.read()
	page.close()
	htmls = html.split(SPLITTER)
	htmls[1] = '\n\n'.join(divs)
	html = SPLITTER.join(htmls)
	page = open(htmlfilename, 'w')
	page.write(html)
	page.close()

listing("audio", "audio/index.html", TEMPLATE_AUDIO)
listing("images", "images/index.html", TEMPLATE_IMAGE)
listing("zips", "zips/index.html", TEMPLATE_ZIP)

def css():
	cssfile = open('index_vars.css', 'r')
	css = cssfile.read()
	cssfile.close()

	cssparts = css.split(SPLITTER)
	vardict = json.loads(cssparts[0])
	css = cssparts[1]

	for variable in vardict:
		css = css.replace(variable + ' ', vardict[variable] + ' ')
		css = css.replace(variable + ';', vardict[variable] + ';')

	cssfile = open('index.css', 'w')
	cssfile.write(css)
	cssfile.close()

css()
