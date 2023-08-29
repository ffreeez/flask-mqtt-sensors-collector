from flask import Flask


app = Flask(__name__)





HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "flask"
PASSWORD = "KhwFMd38s5sixFkx"
DATABASE = "flask"

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column("user_id", db.Integer, primary_key=True)
    user_name = db.Column("user_name", db.String(255), unique=True, nullable=False)
    user_passwd = db.Column("user_passwd", db.String(255), unique=False, nullable=False)

class Device(db.Model):
    __tablename__ = "device"
    device_id = db.Column("device_id", db.Integer, primary_key=True)
    device_uuid = db.Column("device_uuid", db.String(37), unique=True, nullable=False)

class DeviceData(db.Model):
    __tablename__ = "device_data"
    data_id = db.Column("data_id", db.Integer, primary_key=True)
    device_id = db.Column("device_id", db.Integer, nullable=False)
    data_time = db.Column("data_time", db.TIMESTAMP(True), nullable=False, server_default=db.text('CURRENT_TIMESTAMP'), onupdate=db.text('CURRENT_TIMESTAMP'))
    rh = db.Column("rh", db.Float(precision="5, 2"), nullable=False)
    tm = db.Column("tm", db.Float(precision="5, 2"), nullable=False)
    lx = db.Column("lx", db.Float(precision="5, 2"), nullable=False)
    dr = db.Column("dr", db.Float(precision="5, 2"), nullable=False)

class DeviceEvent(db.Model):
    __tablename__ = "device_event"
    event_id = db.Column("event_id", db.Integer, primary_key=True)
    data_time = db.Column("event_time", db.TIMESTAMP(True), nullable=False, server_default=db.text('CURRENT_TIMESTAMP'), onupdate=db.text('CURRENT_TIMESTAMP'))
    user_id = db.Column("user_id", db.Integer, nullable=False)
    device_id = db.Column("device_id", db.Integer, nullable=False)
    event_type = db.Column("event_type", db.Integer, nullable=False)
    event_ok = db.Column("event_ok", db.Integer, nullable=False)

app.secret_key = "1E3166AF53A2"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'





@app.route('/')
def get_users():
    users = User.query.all()
    devices = Device.query.all()
    devicedata = DeviceData.query.all()
    deviceevent = DeviceEvent.query.all()
    return "ok"

@app.route('/login', methods=["POST"])
def register():

if __name__ == '__main__':
    app.run()