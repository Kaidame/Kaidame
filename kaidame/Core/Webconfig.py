import kaidame
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
        if not kaidame.setup_completed:
            raise cherrypy.HTTPRedirect("setup")
        else:
            raise cherrypy.HTTPRedirect("home")
    index.exposed = True

    def setup(self):
        return"Welcome to the setup of {0}<br>" \
              "Please follow below steps to setup the application for use.".format(kaidame.__product__)
    setup.exposed = True

    def home(self):
        return "Hello world!"
        #myDB = database.DBConnection()
        #authors = myDB.select('SELECT * from authors order by AuthorName COLLATE NOCASE')
        #return serve_template(templatename="index.html", title="Home", authors=authors)
    home.exposed = True
