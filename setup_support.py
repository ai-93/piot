import os, json

db_dir = "/home/ubuntu/piot/db.json"

dir_path = os.path.dirname(os.path.realpath(__file__))

class Setup:

    def __init__(self):
        self.db = None
        self.gpio_list = []
        self.mqtt_value = []
        self.is_db_exist = False
        self.db_integrity = False

    def check_if_db_exist(self):
        try:
            self.db = json.load(open(db_dir))
            self.is_db_exist = True
        except:
            pass

    def mqtt_setup(self):
        broker_url = input("Enter broker url(default: io.adafruit.com):") or "io.adafruit.com"
        port = input("Enter the port(default: 1883): ") or  1883
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        refresh_time = input("Enter the refresh time(default 1): ") or  1

        self.mqtt_value = {"broker": broker_url, "port": int(port), "username": username, "password": password, "refresh_time": int(refresh_time)}

    def create_db(self):
        print("MQTT support setup")
        self.mqtt_setup()
        with open(db_dir, 'w') as outfile:
            json.dump({"mqtt": self.mqtt_value}, outfile)
        print("DB setup complete")

    def setup_service(self):
        print("\n Setup piot service \n ##########################\n")
        os.system("sudo cp {}/scrvice/piot.service /lib/systemd/system/".format(dir_path))
        os.system("sudo systemctl enable piot.service")
        print("\n Setup piot service completed \n ##########################\n")

    def start_server(self):
        os.system("sudo systemctl start piot")
        print("Piot Server started")

    def stop_server(self):
        os.system("sudo systemctl stop piot")
        print("Piot Server stopped")

    def restart_server(self):
        os.system("sudo systemctl restart piot")
        print("Piot Server restarted")

    def server_status(self):
        status = os.popen("sudo systemctl status piot")
        print("Piot Server status")
        print(status)

    def server_management(self):
        ck = input("1) Start\n2) Stop\n3) Restart\n4) Status\n\nOption: (default: 4)")

        if int(ck) == 1:
            self.start_server()
        elif int(ck) == 2:
            self.stop_server()
        elif int(ck) == 3:
            self.restart_server()
        else:
            self.server_status()

    def setup_init(self):
        print("DB check")
        self.check_if_db_exist()
        print("DB check completed")
        if not self.is_db_exist:
            self.create_db()

            self.setup_service()
        else:
            if_update = raw_input("Do you want to update(y/n): ")

            if str(if_update).upper() == "Y":
                os.system("bash {}/scripts/update.sh".format(dir_path))

        st = raw_input("Server management(y/n): ")

        if str(st).upper() == "Y":
            self.server_management()



set = Setup()

set.setup_init()
