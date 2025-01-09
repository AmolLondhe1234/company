import os
from company.wsgi import application

if __name__ == "__main__":
    app = application
    port = int(os.environ.get("PORT", 8080))
    
    # Import and configure gunicorn
    import gunicorn.app.base
    
    class StandaloneApplication(gunicorn.app.base.BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            for key, value in self.options.items():
                self.cfg.set(key.lower(), value)

        def load(self):
            return self.application

    options = {
        'bind': f'0.0.0.0:{port}',
        'workers': 2,
        'timeout': 120,
    }

    StandaloneApplication(app, options).run()