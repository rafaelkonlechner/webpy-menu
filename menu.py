# Home is active by default
active = "/"

# Nested list of all desired menu items in this format:
# m = (Url, Name, [m])
# where the first level is the top-level navigation (like a nav-bar) and the
# second level is intended for a dropdown-menu-list
entries =	[
				("/", "Home"),
				("#", "Dropdown", [
					("/blog", "Blog"),
					("/contact", "Contact"),
				]),
			]

def render(nav, dropdown_li, dropdown_a, dropdown_ul):
	"""
	Renders the menu with given html-attributes
	nav: attributes for the top-level list
	dropdown_li: attributes for the wrapping dropdown-list element
	dropdown_a: attributes for dropdown-anchor element
	dropdown_ul: attributes for dropdown-ul element
	"""
	return nest(entries, nav, dropdown_li, dropdown_a, dropdown_ul)

def nest(entries, nav, dropdown_li, dropdown_a, dropdown_ul):
	"""
	Renders the menu with given html-attributes (recursively)
	"""
	nav = "<ul %s>" % parse_attrs(nav)
	for entry in entries:
		url = entry[0]
		name = entry[1]
		if len(entry) == 2:
			nav += "<li %s><a href=\"%s\">%s</a></li>" % (is_active(url), url, name)
		else: # len(entry) == 3: create dropdown element and list children recursively
			nav += "<li %s %s><a %s href=\"%s\">%s</a>%s</li>" % (is_active(url), parse_attrs(dropdown_li), parse_attrs(dropdown_a), url, name, nest(entry[2],dropdown_ul,[],[],[]))
	return nav + '</ul>'

def set_active(url):
	"""
	The active element's html class attribute will become 'active', so css can 
	take care of the design. (e.g. emphasize)
	"""
	global active
	active = url

def is_active(url):
	return "class=\"active\"" if active == url else ""

def parse_attrs(list):
	"""
	Takes a list of (html-attribute, value) tuples and parses respective html
	"""
	attributes = ""
	for attr, val in list:
		attributes += "%s=\"%s\"" % (attr, val)
	return attributes
