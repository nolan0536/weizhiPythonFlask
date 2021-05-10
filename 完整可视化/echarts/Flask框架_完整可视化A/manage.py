from app import create_app
from flask_script import Server,Manager
from flask_migrate import MigrateCommand


# 获取配置
config_name = 'default'
# 创建flask实例
app = create_app(config_name)
# 创建命令行启动控制对象
manager = Manager(app)
manager.add_command("runserver",Server(use_debugger=True))
# 添加数据库迁移命令
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()