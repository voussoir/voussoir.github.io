import os
TEMPLATE = """
		<div class="audioelement">
			<a href="audio/%s">%s</a>
			<audio controls
			  src="audio/%s">
			Your user agent does not support the HTML5 Audio element.
			</audio>
		</div>
"""
SPLITTER = "<!-- Automatic -->"

files = os.listdir("audio")
divs = []
for f in files:
	divs.append(TEMPLATE % (f, f, f))

audiopage = open('audio.html', 'r')
audiohtml = audiopage.read()
audiopage.close()
audiohtmls = audiohtml.split(SPLITTER)
audiohtmls[1] = '\n\n'.join(divs)
audiohtml = SPLITTER.join(audiohtmls)
audiopage = open('audio.html', 'w')
audiopage.write(audiohtml)
audiopage.close()