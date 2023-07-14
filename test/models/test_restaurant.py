from src.models.restaurant import Restaurant
class TestRestaurant:

    def test_describe_restaurant(self):
        # Setup
        restaurant_name = 'Quero_Meu_Churrasco'
        cuisine_type = 'Churrasco'
        resultado_esperado = f"Esse restaturante chama {restaurant_name} e serve {cuisine_type}.Esse restaturante está servindo 0 consumidores desde que está aberto."
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.describe_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_open_restaurant(self):
        # Setup
        restaurant_name = 'Quero_Meu_Churrasco'
        cuisine_type = 'Churrasco'
        resultado_esperado = f"{restaurant_name} agora está aberto!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.open_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_open_restaurant_ja_aberto(self):
        # Setup
        restaurant_name = 'Quero_Meu_Churrasco'
        cuisine_type = 'Churrasco'
        resultado_esperado = f"{restaurant_name} já está aberto!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.open_restaurant()
        resultado = restaurant.open_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_close_restaurant(self):
        # Setup
        restaurant_name = 'Quero_Meu_Churrasco'
        cuisine_type = 'Churrasco'
        resultado_esperado = f"{restaurant_name} agora está fechado!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.close_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_close_restaurant_ja_fechado(self):
        # Setup
        restaurant_name = 'Quero_Meu_Churrasco'
        cuisine_type = 'Churrasco'
        resultado_esperado = f"{restaurant_name} já está fechado!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.close_restaurant()
        resultado = restaurant.close_restaurant()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_set_number_served(self):
        # Setup
        restaurant_name = 'Quero_Meu_Churrasco'
        cuisine_type = 'Churrasco'
        total_customers = '50'
        resultado_esperado = f"Esse restaturante está servindo {total_customers} pessoas atualmente"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.set_number_served(total_customers)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_set_number_served_rest_fechado(self):
        # Setup
        restaurant_name = 'Quero_Meu_Churrasco'
        cuisine_type = 'Churrasco'
        total_customers = '50'
        resultado_esperado = f"{restaurant_name} está fechado!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.set_number_served(total_customers)
        resultado = restaurant.set_number_served(total_customers)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_increment_number_served(self):
        # Setup
        restaurant_name = 'Quero_Meu_Churrasco'
        cuisine_type = 'Churrasco'
        total_customers = '45'
        more_customers = '25'
        resultado_esperado = f"Esse restaturante aumentou para 70 pessoas atendidas"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.increment_number_served(total_customers, more_customers)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_increment_number_served_rest_fechado(self):
        # Setup
        restaurant_name = 'Quero_Meu_Churrasco'
        cuisine_type = 'Churrasco'
        total_customers = '45'
        more_customers = '25'
        resultado_esperado = f"{restaurant_name} está fechado!"
        restaurant = Restaurant(restaurant_name, cuisine_type)

        # Chamada
        resultado = restaurant.increment_number_served(total_customers, more_customers)
        resultado = restaurant.increment_number_served(total_customers, more_customers)

        # Avaliacao
        assert resultado_esperado == resultado
