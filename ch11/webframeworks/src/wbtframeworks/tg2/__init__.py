from tg import expose, TGController, MinimalApplicationConfigurator


class RootController(TGController):
    @expose()
    def index(self):
        return 'Hello World'


def make_application():
    config = MinimalApplicationConfigurator()
    config.update_blueprint({
        'root_controller': RootController()
    })

    return config.make_wsgi_app()
