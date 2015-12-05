import web
from web import form
from convert_country import *


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
        return render.result({
                                "title": country.replace("-", " ").capitalize(),
                                "image": image,
                                "url_to_graph_crude": "../static/svg/" +  full_to_short_country(country.replace(" ", "-")) + "_Death_rate_crude_(per_1000_people).svg",
                                "url_to_graph_under_five": "../static/svg/" +  full_to_short_country(country.replace(" ", "-")) + "_Number_of_under-five_deaths.svg",
                                "url_to_graph_injury": "../static/svg/" +  full_to_short_country(country.replace(" ", "-")) + "_Cause_of_death_by_injury_(%_of_total).svg",
                                "url_to_graph_battle": "../static/svg/" +  full_to_short_country(country.replace(" ", "-")) + "_Battle-related_deaths_(number_of_people).svg",
                                "url_to_graph_population": "../static/svg/" +  full_to_short_country(country.replace(" ", "-")) + "_Population_total.svg"
                            })

class Country:
    def GET(self, name=None):
        return render.country()

class About:
    def GET(self, name=None):
        return render.about()

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
