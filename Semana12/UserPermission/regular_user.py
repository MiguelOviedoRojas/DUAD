from user_class import User

class RegularUser(User):
    def __init__(self, name):
        super().__init__()
        self.name = name.upper()
    
    def get_role(self, user_permission):
        list_admin_permission = ["read"]
        for permission in list_admin_permission:
            if user_permission == permission:
                return True
        return False

    def has_permission(self, permission):
        response = self.get_role(permission)
        if response == True:
            return(f"User {self.name} has Permission for Regular User for {permission}")
        else:
            return(f"User doesn't has Permission: {permission}")
