#!/usr/bin/python

import web, menu

#optional:
web.config.debug = True

urls =	(
			'/', 'Index',
			'/blog', 'Blog',
			'/contact', 'Contact'
		)

app = web.application(urls, globals())

# register menu for global use in templates
globals_ = {
	'menu': menu,
}

render = web.template.render('templates/', base='base', globals = globals_)

class Index:
	def GET(self):
		return render.index()

class Blog:
	def GET(self):
		return render.blog()

class Contact:
	def GET(self):
		return render.contact()

def set_menu():
	"""
	Loadhook method (executed before every request handling)
	If requested URL (path) matches an element in the menu-list, this menu-element is
	set to 'active' (e.g. class="active"), and css takes care of proper design.
	"""
	menu.set_active(web.ctx.path)

app.add_processor(web.loadhook(set_menu))

if __name__ == "__main__":
	app.run()
