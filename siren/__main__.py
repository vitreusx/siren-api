from siren.app import create_app

if __name__ == "__main__":
    app = create_app()
    host = app.config.get("HOST", "0.0.0.0")
    port = app.config.get("PORT", "5000")
    app.run(host=host, port=port)
