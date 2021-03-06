from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

class TestAPI:

    '''TODOS OS TESTES SEGUEM VIRTUALMENTE O MESMO MODELO, MUDANDO ALGUMAS INFORMAÇÕES ESPECÍFICAS ENTRE PRÉ-DETERMINAD_
    AS E ALEATÓRIAS, POR CONTA DA MAIOR PROBABILIDADE DE SUCESSO CASO UM NÚMERO 'X' SEJA ALEATÓRIO
    POR CONTA DA ALEATORIDADE DE ALGUNS TESTES, EU INCLUI UMA IMAGEM CHAMADA 'ALL_ASSERTS_POSITIVE_LOG' QUE CONTÉM UM
    PRINT DE UMA DAS VEZES EM QUE CONSEGUI QUE TODOS OS TESTES RETORNASSEM POSITIVOS, SOMENTE PARA PROVAR QUE É POSSÍ_
    VEL'''

    def test_get(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        driver.implicitly_wait(1)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        api_url = 'https://gorest.co.in/public/v1/users'

        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[0])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        """O response code correto varia dependendo do teste"""
        assert response_code == 'Response: 200'

        driver.close()

    def test_get_by_id(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        driver.implicitly_wait(1)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        random_number = str(random.randrange(2, 3000))
        random_number = str(random_number)
        api_url = 'https://gorest.co.in/public/v1/users/{}'.format(random_number)

        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[0])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 200'

        driver.close()

    def test_post(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        driver.implicitly_wait(1)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        random_number = str(random.randrange(2, 3000))
        random_number = str(random_number)
        api_url = 'https://gorest.co.in/public/v1/users'
        request = '{"name":"V", "gender":"male", "email":"v@gmail.com", "status":"active"}'
        request = request.replace("v", random_number, 1)

        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[1])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').send_keys(request)
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 201'

        driver.close()

    def test_put(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        driver.implicitly_wait(1)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        random_number = random.randrange(2, 3000)
        random_number = str(random_number)
        api_url = 'https://gorest.co.in/public/v1/users/2'
        request = '{"name":"V", "gender":"male", "email":"x@gmail.com", "status":"active"}'
        request = request.replace("x", random_number)

        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[2])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').send_keys(request)
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 200'

        driver.close()

    def test_delete(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        driver.implicitly_wait(1)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        random_id = random.randrange(2, 3000)
        api_url = ('https://gorest.co.in/public/v1/users/{}'.format(random_id))

        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[4])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 204'

        driver.close()

    def test_nested_posts_get(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        random_number = str(random.randrange(2, 3000))
        random_number = str(random_number)
        api_url_posts = 'https://gorest.co.in/public/v1/users/{}/posts'
        api_url_posts = api_url_posts.replace('{}', random_number)

        """POSTS GET"""
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[0])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url_posts)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 200'

    def test_nested_posts_post(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        random_number = str(random.randrange(2, 3000))
        random_number = str(random_number)
        api_url_posts = 'https://gorest.co.in/public/v1/users/{}/posts'
        api_url_posts = api_url_posts.replace('{}', random_number)
        request_post_post = '{"id":1,"user_id":2,"title":"Hello","body":"Hi"}'

        """POSTS POST"""

        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[1])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url_posts)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').send_keys(request_post_post)
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 201'

    def test_nested_comments_get(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        api_url_comments = 'https://gorest.co.in/public/v1/posts/1/comments'

        """COMMENTS GET"""
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[0])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url_comments)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 200'

    def test_nested_comments_post(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        request_post_comment = '{"name":"V", "email":"v@gmail.com", "body":"Hi"}'
        api_url_comments = 'https://gorest.co.in/public/v1/posts/1/comments'

        """COMMENTS POST"""
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[1])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url_comments)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').send_keys(request_post_comment)
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 201'

    def test_nested_todos_get(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        api_url_todos = 'https://gorest.co.in/public/v1/users/2/todos'

        """TODOS GET"""
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[0])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url_todos)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 200'

    def test_nested_todos_post(self):

        """Universais"""
        driver = webdriver.Chrome()
        api_console_url = 'https://gorest.co.in/rest-console'
        access_token = 'Bearer 217e3301cc89e0aa66a6b40ba6880779bbd462ee0ae696e65b679ff8d46d0af6'
        driver.get(api_console_url)
        option = [1, 2, 3, 4, 5, 6, 7]

        """Únicos"""
        random_number = str(random.randrange(2, 3000))
        random_number = str(random_number)
        api_url_todos = 'https://gorest.co.in/public/v1/users/{}/todos'
        api_url_todos = api_url_todos.replace('{}', random_number)
        request_post_todo = '{"id":1,"user_id":2,"title":"Except Due Date.","due_on":"2021-12-26T00:00:00.000+05:30",' \
                            '"status":"pending"}'


        """TODOS POST"""
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_type"] / option[{}]'.format(option[1])).click()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_url"]').send_keys(api_url_todos)
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').clear()
        driver.find_element(By.XPATH, '// *[ @ id = "rsq_header_value_0"]').send_keys(access_token)
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').clear()
        driver.find_element(By.XPATH, '//*[@id="rsq_body"]').send_keys(request_post_todo)
        driver.find_element(By.XPATH, '//*[@id="rsq_send"]').click()

        time.sleep(3)

        response_code = driver.find_element(By.XPATH, '//*[@id="rsp-body-title"]').text

        assert response_code == 'Response: 201'

        driver.close()
