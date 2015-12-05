import web
from web import form

render = web.template.render('templates/', base='layout')

urls = (
            '/?', 'Index',
            '/result/?(.+)', 'Result',
            '/country/?', 'Country',
            '/about/?', 'About'
        )

class Index:
    def GET(self, name=None):
        return render.index()
    def POST(self):
        country = web.input()
        raise web.seeother("result/" + country.country)

class Result:
    def GET(self, country):
        image = country.lower() + ".svg"
        return render.result(country, image)

class Country:
    def GET(self, name=None):
        return render.country()

class About:
    def GET(self, name=None):
        return render.about()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
