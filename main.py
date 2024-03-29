from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8999  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        with open('index.html', 'r', encoding='utf8') as file:
            html_data = file.read()
            return html_data


    """Специальный класс, который отвечает за обработку входящих запросов от клиентов"""

    def do_GET(self):
        """ Метод для обработки входящих GET-запросов """
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        page_content = self.__get_html_content()
        self.send_response(200)
        self.send_header("Content-type", "text/html")  # Отправка типа данных, который будет передаваться
        self.end_headers()  # Завершение формирования заголовков ответа
        self.wfile.write(bytes(page_content, "utf-8"))  # Тело ответа


if __name__ == "__main__":

    """Инициализация веб-сервера, который будет по заданным параметрам в сети
     принимать запросы и отправлять их на обработку специальному классу, который был описан выше"""

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        """Cтарт веб-сервера в бесконечном цикле прослушивания входящих запросов"""
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    """Корректная остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал"""
    webServer.server_close()
