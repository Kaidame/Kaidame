import kaidame
#import kaidame.Lib.cherrypy as cherrypy
import cherrypy

import os

# def serve_template(templatename, **kwargs):
#
#     interface_dir = os.path.join(str(lazylibrarian.PROG_DIR), 'data/interfaces/')
#     template_dir = os.path.join(str(interface_dir), lazylibrarian.HTTP_LOOK)
#     _hplookup = TemplateLookup(directories=[template_dir])
#
#
#     try:
#         template = _hplookup.get_template(templatename)
#         return template.render(**kwargs)
#     except:
#         return exceptions.html_error_template().render()


class WebInterface(object):

    def index(self):
        print "Test"
        raise cherrypy.HTTPRedirect("home")
    index.exposed = True

    def home(self):
        return "Hello world!"
        #myDB = database.DBConnection()
        #authors = myDB.select('SELECT * from authors order by AuthorName COLLATE NOCASE')
        #return serve_template(templatename="index.html", title="Home", authors=authors)
    home.exposed = True
