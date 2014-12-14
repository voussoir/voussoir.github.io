import os
TEMPLATE_AUDIO = """
		<div class="audioelement">
			<a href="audio/{f}">{f}</a>
			<audio controls
			  src="audio/{f}">
			Your user agent does not support the HTML5 Audio element.
			</audio>
		</div>
"""
TEMPLATE_IMAGE = """
		<div class="imagelinkelement">
			<a href="images/{f}">{f}</a>
		</div>
"""
SPLITTER = "<!-- Automatic -->"

def listing(directory, htmlfilename, template):
	files = os.listdir(directory)
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

listing("audio", "audio.html", TEMPLATE_AUDIO)
listing("images", "images.html", TEMPLATE_IMAGE)