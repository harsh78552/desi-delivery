from .add_to_cart import blp as UserAddItemBlueprint
from .fetch_add_to_cart_item import blp as UserFetchAllItemBlueprint
from .fetch_total_item_add_in_cart import blp as UserFetchItemBlueprint
from .get_all_ordered import blp as UserAllOrderedFood
from .get_food_data import blp as GetFoodItemBlueprint
from .update_profile import blp as ProfileUpdateBlueprint
from .user_food_order import blp as UserOrderFoodBlueprint
from .user_login import blp as UserLoginBlueprint
from .user_profile import blp as UserProfileBlueprint
from .user_register import blp as UserRegistrationBlueprint


def register_user_blueprint(app_api):
    app_api.register_blueprint(GetFoodItemBlueprint)
    app_api.register_blueprint(UserRegistrationBlueprint)
    app_api.register_blueprint(UserLoginBlueprint)
    app_api.register_blueprint(UserProfileBlueprint)
    app_api.register_blueprint(UserFetchItemBlueprint)
    app_api.register_blueprint(ProfileUpdateBlueprint)
    app_api.register_blueprint(UserOrderFoodBlueprint)
    app_api.register_blueprint(UserAddItemBlueprint)
    app_api.register_blueprint(UserAllOrderedFood)
    app_api.register_blueprint(UserFetchAllItemBlueprint)
