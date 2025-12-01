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


def register_admin_blueprint(api):
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
