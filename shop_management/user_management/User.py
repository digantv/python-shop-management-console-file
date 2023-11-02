class User:
    def __init__(self, userName=None, loginName=None, password=None, confirmPassword=None,
                 userRole=None):  # Constructor
        self.userName = userName
        self.loginName = loginName
        self.password = password
        self.confirmPassword = confirmPassword
        self.userRole = userRole
