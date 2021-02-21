def data(file_name):
        with open(file_name, encoding="latin-1") as file:
                slack_data = file.read()
        string = ""
        strings = []
        for i in slack_data:
                if i.isprintable():
                        if i != '"':
                                string += i
                        else:
                                strings.append(string)
                                string = ""
        while("" in strings) :
                strings.remove("")
        data = {}
        real_name = ""
        for i in range(len(strings)):
                if strings[i] == "real_name":
                        real_name = strings[i+1]
                        data[real_name]=[]
                elif real_name == "" or real_name == strings[i]:
                        continue
                else:
                        if len(data[real_name]) < 80:
                                data[real_name].append(strings[i])
        return strings, data
def users(properties):
        users = {}
        infos = ["Email", "Profile Picture", "Bot", "Admin", "Owner", "Primary Owner"]
        for username in properties:
                users[username] = {}
                for i in range(len(properties[username])):
                        if properties[username][i] == "email":
                                users[username]["Email"] = properties[username][i+1]
                        elif properties[username][i] == "image_1024":
                                users[username]["Profile Picture"] = properties[username][i+1][1:-1]
                        elif properties[username][i] == "is_botT":
                                users[username]["Bot"] = "True"
                        elif properties[username][i] == "is_adminT":
                                users[username]["Admin"] = "True"
                        elif properties[username][i] == "is_ownerT":
                                users[username]["Owner"] = "True"
                        elif properties[username][i] == "is_primary_ownerT":
                                users[username]["Primary Owner"] = "True"
                        elif properties[username][i] == "is_botF":
                                users[username]["Bot"] = "False"
                        elif properties[username][i] == "is_adminF":
                                users[username]["Admin"] = "False"
                        elif properties[username][i] == "is_ownerF":
                                users[username]["Owner"] = "False"
                        elif properties[username][i] == "is_primary_ownerF":
                                users[username]["Primary Owner"] = "False"
        for user in users:
                for info in infos:
                        if info not in users[user]:
                                users[user][info] = "404 Not Found"
        print("{:<30} {:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format('Users', 'Email', "is_bot", "is_admin", "is_owner", "primary_owner", 'Profile Picture'))
        for user in users:
                print("{:<30} {:<30} {:<30} {:<30} {:<30} {:<30} {:<30}".format(user, users[user]["Email"], users[user]["Bot"], users[user]["Admin"], users[user]["Owner"], users[user]["Primary Owner"] ,users[user]["Profile Picture"]))
        return
def messages(data):
        for i in range(len(data)):
                if data[i] == 'text' and data[i+1] == 'text':
                        print(str(data[i+2]))
        return
def workspace(data):
        infos = {"domain":"", "channels":[]}
        for i in range(len(data)):
                if data[i] == "name" and data[i+2] == "is_channelT":
                        infos["channels"].append(data[i+1])
                elif data[i] == "domain":
                        infos["domain"] = data[i+1]
        for key, value in infos.items():
                print(f"{key}: {value}")
        return
if __name__ == '__main__':
        print('''
   _____ _            _           _____                         
  / ____| |          | |         |  __ \                        
 | (___ | | __ _  ___| | ________| |__) |_ _ _ __ ___  ___ _ __ 
  \___ \| |/ _` |/ __| |/ /______|  ___/ _` | '__/ __|/ _ \ '__|
  ____) | | (_| | (__|   <       | |  | (_| | |  \__ \  __/ |   
 |_____/|_|\__,_|\___|_|\_\      |_|   \__,_|_|  |___/\___|_|     
                                                By: 0xMohammed''')
        try:
                indexeddb = input("Insert Slack Database Path (%appdata%\\Slack\\IndexedDB\\https_app.slack.com_0.indexeddb.blob\\*): ")
                strings, data = data(indexeddb)
        except:
                print("Please Enter a valid Slack Database")
                exit()
        while 1:
                        function_name = input("Insert the data you want (users, messages, workspace): ")
                        if function_name == "users":
                                eval(function_name + "(data)")
                        elif function_name in ["users", "messages","workspace","exit"]:
                                eval(function_name + "(strings)")
                        else:
                                print("Error occurred Try-Again")
