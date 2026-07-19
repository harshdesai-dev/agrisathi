from flask import Flask, app, redirect, url_for
from config import Config
import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    

    db.init_app(app)

    import auth
    import dashboard
    import schemes
    import prices

    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(schemes.bp)
    app.register_blueprint(prices.bp)

    @app.route("/")
    def home():
        return redirect(url_for("dashboard.index"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
