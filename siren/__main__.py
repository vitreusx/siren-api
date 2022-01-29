from siren.app import create_app

if __name__ == "__main__":
    app = create_app()
    host = app.config.get("FLASK_HOST", "0.0.0.0")
    port = app.config.get("FLASK_PORT", "5000")
    app.run(host=host, port=port)
