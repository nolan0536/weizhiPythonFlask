from app import create_app
from flask_script import Server,Manager
from flask_migrate import MigrateCommand

# 获取配置
config_name = "default"
# 创建Flask实例
app = create_app(config_name)
# 添加命令控制语句
manager = Manager(app)
# 添加数据库迁移命令
manager.add_command("runserver",Server(use_debugger=True))
# 添加db命令
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    app.run(debug=True)