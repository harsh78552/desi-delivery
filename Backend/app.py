from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, unset_jwt_cookies
from flask_mail import Mail
from flask_smorest import Api

from UserApi.add_to_cart import blp as UserAddItemBlueprint
from UserApi.get_all_ordered import blp as UserAllOrderedFood
from UserApi.get_food_data import blp as GetFoodItemBlueprint
from UserApi.update_profile import blp as ProfileUpdateBlueprint
from UserApi.user_food_order import blp as UserOrderFoodBlueprint
from UserApi.user_login import blp as UserLoginBlueprint
from UserApi.user_profile import blp as UserProfileBlueprint
from UserApi.user_register import blp as UserRegistrationBlueprint
from adminApi.admin_delete_food import blp as AdminDeleteFoodItemBlueprint
from adminApi.admin_edit_food_data import blp as AdminEditFoodDataBlueprint
from adminApi.admin_login import blp as AdminLoginBlueprint
from adminApi.admin_logout import blp as AdminLogoutBlueprint
from adminApi.delete_staff import blp as AdminDeleteStaffBlueprint
from adminApi.food_data import blp as AdminInsertFoodDataBlueprint
from adminApi.get_all_order_data import blp as AdminGetAllOrderBlueprint
from adminApi.get_all_staff import blp as AdminGetAllStaffData
from adminApi.get_food import blp as AdminGetAllFoodBlueprint
from adminApi.staff_registeration import blp as AdminStaffRegistrationBlueprint
from adminApi.update_staff_data import blp as AdminUpdateStaffBlueprint

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": ["https://desi-delivery.vercel.app"]}}, supports_credentials=True)

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
# # app.config['JWT_COOKIE_SECURE'] = False
# app.config['JWT_ACCESS_COOKIE_PATH'] = '/'
# app.config['JWT_REFRESH_COOKIE_PATH'] = '/refresh'
# app.config['JWT_COOKIE_CSRF_PROTECT'] = False
# app.config["JWT_COOKIE_SAMESITE"] = 'Lax'
# app.config['JWT_COOKIE_HTTPONLY'] = True

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
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

api = Api(app)
jwt = JWTManager(app)

api.register_blueprint(GetFoodItemBlueprint)
api.register_blueprint(UserRegistrationBlueprint)
api.register_blueprint(UserLoginBlueprint)
api.register_blueprint(UserProfileBlueprint)
api.register_blueprint(ProfileUpdateBlueprint)
api.register_blueprint(UserOrderFoodBlueprint)
api.register_blueprint(UserAddItemBlueprint)
api.register_blueprint(UserAllOrderedFood)
api.register_blueprint(AdminLoginBlueprint)
api.register_blueprint(AdminLogoutBlueprint)
api.register_blueprint(AdminInsertFoodDataBlueprint)
api.register_blueprint(AdminStaffRegistrationBlueprint)
api.register_blueprint(AdminDeleteStaffBlueprint)
api.register_blueprint(AdminUpdateStaffBlueprint)
api.register_blueprint(AdminGetAllOrderBlueprint)
api.register_blueprint(AdminGetAllFoodBlueprint)
api.register_blueprint(AdminEditFoodDataBlueprint)
api.register_blueprint(AdminDeleteFoodItemBlueprint)
api.register_blueprint(AdminGetAllStaffData)


@app.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to see if the API is running.
    """
    return jsonify({
        "status": "success",
        "message": "API is working properly!"
    }), 200


if __name__ == "__main__":
    app.run()
