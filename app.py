
# registro i blue print i blueprint creati nei vari gruppi di controller
from core.config import app
from core.controllers.auth.authController import auth
from core.controllers.dashboard.dashboardController import dashboard
from core.controllers.main.mainController import main

app.register_blueprint(main)
app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(dashboard)

if __name__ == '__main__':
    app.run(debug=True)

