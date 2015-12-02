import web

render = web.template.render('templates/', base='layout')

urls = (
            '/', 'Index',
            '/result', 'Result',
            '/country', 'Country',
            '/about', 'About'
        )

class Index:
    def GET(self, name=None):
        return render.index()

class Result:
    def GET(self, name=None):
        return render.result()

class Country:
    def GET(self, name=None):
        return render.country()

class About:
    def GET(self, name=None):
        return render.about()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
