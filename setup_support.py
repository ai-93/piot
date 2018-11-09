import os, json
from tinydb import TinyDB, Query
from gpio_support import get_pin_status

dir_path = os.path.dirname(os.path.realpath(__file__))

# db = TinyDB('{}/db.json'.format(dir_path))


class Setup:

    def __init__(self):
        self.db = None
        self.gpio_list = []
        self.is_db_exist = False
        self.db_integrity = False

    def check_if_db_exist(self):
        try:
            self.db = json.load(open("db.json"))
            self.is_db_exist = True
        except:
            pass

    def check_db_integrity(self):
        if "gpio" in self.db.keys():
            pass

    def gpio_setup(self):
        while True:
            name = input("Enter the name: ")
            pin = input("Enter GPIO pin: ")
            location = input("Enter location: ")

            continu = input("Do you want to add more switches (y/n): ")

            self.gpio_list.append({"name": name, "pin": pin, "location": location})

            if continu.upper() == "N":
                break




    def mqtt_setup(self):
        pass

    def create_db(self):
        self.gpio_setup()
        self.mqtt_setup()

    def setup_init(self):
        self.check_if_db_exist()

        if self.is_db_exist:
            self.check_db_integrity()
            if self.db_integrity:
                pass
            else:
                pass
        else:
            self.create_db()

print(dir_path)
set = Setup()

set.setup_init()

# def gpioadd(pin, name, default_state, etype, finish):
#     print ("in gpio add")
#
#     if finish =='on':
#         table = db.table('info')
#         servername = table.all()[0]['name']
#         db.purge_table('info')
#
#         table.insert(
#                 {
#                     'name': servername,
#                     'local_address': '',
#                     'public_address': '',
#                     'is_auth_setup': True,
#                     'is_gpio_config_complete': True,
#                     'is_mqtt_config_complete': True,
#                     'is_public_access_config_complete': False,
#                     'is_initial': False
#                 }
#             )
#
#     table = db.table('gpio')
#     table.insert(
#                 {
#                     'pin': pin,
#                     'name': name,
#                     'default_state': default_state,
#                     'etype': etype,
#                     'current_state': get_pin_status(int(pin))
#                 }
#             )
#
# def publicaccesssetup(enable):
#     print ("in public access setup")
#
#     if enable:
#         table = db.table('info')
#         servername = table.all()[0]
#
#         servername = servername['name']
#         db.purge_table('info')
#         table = db.table('info')
#         table.insert(
#                     {
#                         'name': servername,
#                         'local_address': '',
#                         'public_address': 'https://{}.serveo.net'.format(servername),
#                         'is_auth_setup': True,
#                         'is_gpio_config_complete': True,
#                         'is_mqtt_config_complete': True,
#                         'is_public_access_config_complete': True,
#                         'is_initial': False
#                     }
#                 )
#     else:
#         table = db.table('info')
#         servername = table.all()[0]
#
#         servername = servername['name']
#         db.purge_table('info')
#         table = db.table('info')
#         table.insert(
#                     {
#                         'name': servername,
#                         'local_address': '',
#                         'public_address': '',
#                         'is_auth_setup': True,
#                         'is_gpio_config_complete': True,
#                         'is_mqtt_config_complete': True,
#                         'is_public_access_config_complete': True,
#                         'is_initial': False
#                     }
#                 )
#
# def mqttSetup(broker, port, username, password):
#     print ("in mqtt setup")
#     table = db.table('info')
#     servername = table.all()[0]
#
#     servername = servername['name']
#     db.purge_table('info')
#     table = db.table('info')
#     table.insert(
#                 {
#                     'name': servername,
#                     'local_address': '',
#                     'public_address': '',
#                     'is_auth_setup': True,
#                     'is_gpio_config_complete': False,
#                     'is_mqtt_config_complete': True,
#                     'is_public_access_config_complete': False,
#                     'is_initial': False
#                 }
#             )
#     table = db.table('mqtt')
#     table.insert(
#                 {
#                     'broker': broker,
#                     'port': port,
#                     'username': username,
#                     'password': password
#                 }
#             )
#
#
# def onboard_user(servername, username, password):
#     print ("in onboard")
#     table = db.table('info')
#     db.purge_table('info')
#     table = db.table('info')
#     table.insert(
#                 {
#                     'name': servername,
#                     'local_address': '',
#                     'public_address': '',
#                     'is_auth_setup': True,
#                     'is_gpio_config_complete': False,
#                     'is_mqtt_config_complete': False,
#                     'is_public_access_config_complete': False,
#                     'is_initial': False
#                 }
#             )
#     table = db.table('user')
#     table.insert(
#                 {
#                     'username': username,
#                     'password': password
#                 }
#             )
#
# def getgpio_list():
#     table = db.table('gpio')
#     glist = table.all()
#     return glist
#
#
# def get_setup_stage():
#     table = db.table('info')
#     info = table.all()
#
#     if info[0]['is_initial']:
#         return "is_initial"
#     elif not info[0]['is_auth_setup']:
#         return 'is_auth_setup'
#     elif not info[0]['is_mqtt_config_complete']:
#         return 'is_mqtt_config_complete'
#     elif not info[0]['is_gpio_config_complete']:
#         return 'is_gpio_config_complete'
#     elif not info[0]['is_public_access_config_complete']:
#         return 'is_public_access_config_complete'
#     else:
#         return 'index'
#
#
# def is_initial():
#     table = db.table('info')
#     info = table.all()
#
#     if not info[0]['is_initial'] and info[0]['is_public_access_config_complete']:
#         return False
#     else:
#         return True
#
#
# def setup_db():
#     table = db.table('info')
#     info = table.all()
#     if info == []:
#         table.insert(
#                 {
#                     'name': '',
#                     'local_address': '',
#                     'public_address': '',
#                     'is_auth_setup': False,
#                     'is_gpio_config_complete': False,
#                     'is_mqtt_config_complete': False,
#                     'is_public_access_config_complete': False,
#                     'is_initial': True
#                 }
#             )
#     print (info)