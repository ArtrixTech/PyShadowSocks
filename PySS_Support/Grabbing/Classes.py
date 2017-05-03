import requests
from PySS_Support.Functions import cut_string
from PySS_Support.Classes import SSServer


def get_all_server(debug=False):

    if not debug:
        all_server_collection = list()
        content = requests.get("https://freessr.xyz").text
        all_html_list = content.split("<div class=\"col-md-6 text-center\">")
        all_html_list.pop(0)

        # add all server to the server list
        for html in all_html_list:

            server = SSServer()
            ip = cut_string(html, "服务器地址:", "</h4>")
            port = cut_string(html, "端口:", "</h4>")
            password = cut_string(html, "密码:", "</h4>")
            encryption = cut_string(html, "加密方式:", "</h4>")

            try:
                server.ip = ip
                server.port = port
                server.password = password
                server.encryption = encryption
                all_server_collection.append(server)
                print("Get Server\"%s\":%s" % (server.ip, server))
            except ValueError:
                pass

        return all_server_collection
    else:
        all_server_collection = list()
        content = open("E:/工程文件/Python/PySS/1.html",mode="r",encoding="utf-8").read()
        all_html_list = content.split("<div class=\"col-md-6 text-center\">")
        all_html_list.pop(0)

        # add all server to the server list
        for html in all_html_list:

            server = SSServer()
            ip = cut_string(html, "服务器地址:", "</h4>")
            port = cut_string(html, "端口:", "</h4>")
            password = cut_string(html, "密码:", "</h4>")
            encryption = cut_string(html, "加密方式:", "</h4>")

            try:
                server.ip = ip
                server.port = port
                server.password = password
                server.encryption = encryption
                all_server_collection.append(server)
                print("Get Server\"%s\":%s" % (server.ip, server))
            except ValueError:
                pass

        return all_server_collection
