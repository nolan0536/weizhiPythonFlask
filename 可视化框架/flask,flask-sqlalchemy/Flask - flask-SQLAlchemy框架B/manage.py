from app import create_app
from flask_script import Server,Manager
from flask_migrate import MigrateCommand

# 获取配置信息
config_name = "default"
# 创建app对象
app = create_app(config_name)
# 创建命令行启动控制对象
manage = Manager(app)
manage.add_command("runserver",Server(use_debugger=True))
# 添加数据库迁移命令
manage.add_command(MigrateCommand)
# 启动项目
if __name__ == '__main__':
    manage.run()