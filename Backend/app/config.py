def configure_app(app):
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config['API_TITLE'] = 'Food Ordering System'
    app.config['API_VERSION'] = 'v1'
    app.config['OPENAPI_VERSION'] = '3.0.3'
    app.config['OPENAPI_URL_PREFIX'] = '/'
    app.config['OPENAPI_SWAGGER_UI_PATH'] = "/swagger-ui"
    app.config['OPENAPI_SWAGGER_UI_URL'] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config['JWT_SECRET_KEY'] = 'harsh8926466446jhgsfblsgwogw4lb'
    app.config['SECRET_KEY'] = 'HARSH79565hergitgbslvwfcbiew'

    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'

    # Email
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'ht728350@gmail.com'
    app.config['MAIL_PASSWORD'] = "hnzx xeiq sqcj vglh"

    app.config['API_SPEC_OPTIONS'] = {
        "components": {
            "securitySchemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT"
                }
            }
        },
        "security": [{"bearerAuth": []}]
    }
