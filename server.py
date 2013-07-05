import os
import urllib2

import web
from jinja2 import FileSystemLoader, Environment

url = urls = (
    "/", "Index",
    "/load_page", "LoadPage")

app = web.application(urls, globals())

jinja_env = Environment(
    loader=FileSystemLoader(os.path.dirname(__file__)))


class Index:
    def GET(self):
        return jinja_env.get_template("wordcloud.html").render({})


class LoadPage:
    def GET(self):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        infile = opener.open("http://en.wikipedia.org/wiki/Facebook")
        page = infile.read()
        return page

if __name__ == "__main__":
    app.run()
