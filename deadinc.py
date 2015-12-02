import web

render = web.template.render('templates/', base='layout')

urls = (
            '/', 'index',
            '/result', 'result'
        )

class index:
    def GET(self, name=None):
        return render.index()

class result:
    def GET(self, name=None):
        return render.result()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
