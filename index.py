import web

render = web.template.render('templates/')

urls = (
    '/(.*)', 'index'
)

class index:
    def GET(self, name=None):
        return render.template()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
