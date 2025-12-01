from .admin_delete_food import blp as AdminDeleteFoodItemBlueprint
from .admin_edit_food_data import blp as AdminEditFoodDataBlueprint
from .admin_login import blp as AdminLoginBlueprint
from .admin_logout import blp as AdminLogoutBlueprint
from .delete_staff import blp as AdminDeleteStaffBlueprint
from .food_data import blp as AdminInsertFoodDataBlueprint
from .get_all_order_data import blp as AdminGetAllOrderBlueprint
from .get_all_staff import blp as AdminGetAllStaffData
from .get_food import blp as AdminGetAllFoodBlueprint
from .staff_registeration import blp as AdminStaffRegistrationBlueprint
from .update_staff_data import blp as AdminUpdateStaffBlueprint


def register_admin_blueprint(app_api):
    app_api.register_blueprint(AdminLoginBlueprint)
    app_api.register_blueprint(AdminLogoutBlueprint)
    app_api.register_blueprint(AdminInsertFoodDataBlueprint)
    app_api.register_blueprint(AdminStaffRegistrationBlueprint)
    app_api.register_blueprint(AdminDeleteStaffBlueprint)
    app_api.register_blueprint(AdminUpdateStaffBlueprint)
    app_api.register_blueprint(AdminGetAllOrderBlueprint)
    app_api.register_blueprint(AdminGetAllFoodBlueprint)
    app_api.register_blueprint(AdminEditFoodDataBlueprint)
    app_api.register_blueprint(AdminDeleteFoodItemBlueprint)
    app_api.register_blueprint(AdminGetAllStaffData)
