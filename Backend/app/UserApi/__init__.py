from .add_to_cart import blp as UserAddItemBlueprint
from .fetch_add_to_cart_item import blp as UserFetchAllItemBlueprint
from .fetch_add_to_cart_item import blp as UserFetchItemBlueprint
from .get_all_ordered import blp as UserAllOrderedFood
from .get_food_data import blp as GetFoodItemBlueprint
from .update_profile import blp as ProfileUpdateBlueprint
from .user_food_order import blp as UserOrderFoodBlueprint
from .user_login import blp as UserLoginBlueprint
from .user_profile import blp as UserProfileBlueprint
from .user_register import blp as UserRegistrationBlueprint


def register_user_blueprint(api):
    api.register_blueprint(GetFoodItemBlueprint)
    api.register_blueprint(UserRegistrationBlueprint)
    api.register_blueprint(UserLoginBlueprint)
    api.register_blueprint(UserProfileBlueprint)
    api.register_blueprint(UserFetchItemBlueprint)
    api.register_blueprint(ProfileUpdateBlueprint)
    api.register_blueprint(UserOrderFoodBlueprint)
    api.register_blueprint(UserAddItemBlueprint)
    api.register_blueprint(UserAllOrderedFood)
    api.register_blueprint(UserFetchAllItemBlueprint)
