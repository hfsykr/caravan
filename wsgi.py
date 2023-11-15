from dotenv import load_dotenv
import os
from app import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

load_dotenv()

app = create_app()

if os.getenv("REVERSE_PROXY", "Flase").lower() == "true":
    app.wsgi_app = ProxyFix(app.wsgi_app, x_host=1, x_prefix=1, x_for=1, x_proto=1)

if __name__ == "__main__":
    app.run()