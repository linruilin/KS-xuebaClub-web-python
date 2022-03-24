import jwt
from app.model.userModel import UserModel


class Token(UserModel):  # 验证是否登录

    def __init__(self):
        UserModel.__init__(self)

    def valiToken(self, request):  # 验证是否登录
        try:
            user_token = request.cookies.get('user_token')
            if user_token is None:
                return False
            userData = jwt.decode(user_token, 'secret', algorithms=['HS256'])
            loginType = self.isLogin(userData)
            return loginType
            
        except Exception as e:
            return False
