from src.models.ice_cream_stand import IceCreamStand

class TestIceCreamStand:

    def test_flavors_available_with_flavors(self):
        # Setup
        restaurant_name = 'Delicia_De_Sorvete'
        cuisine_type = 'Sorvete'
        flavors_list = ['Flocos', 'Morango', 'Chocolate', 'Sensacao', 'Menta']
        resultado_esperado = f"No momento temos os seguintes sabores de sorvete disponíveis: {flavors_list}"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.flavors_available()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_flavors_available_no_flavors(self):
        # Setup
        restaurant_name = 'Delicia_De_Sorvete'
        cuisine_type = 'Sorvete'
        flavors_list = []
        resultado_esperado = "Estamos sem estoque atualmente!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.flavors_available()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_find_flavor_sucesso(self):
        # Setup
        restaurant_name = 'Delicia_De_Sorvete'
        cuisine_type = 'Sorvete'
        flavors_list = ['Flocos', 'Morango', 'Chocolate', 'Sensacao', 'Menta']
        flavor = 'Chocolate'
        resultado_esperado = f"Temos no momento {flavor}!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.find_flavor(flavor)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_find_flavor_sem_sucesso(self):
        # Setup
        restaurant_name = 'Delicia_De_Sorvete'
        cuisine_type = 'Sorvete'
        flavors_list = ['Flocos', 'Morango', 'Chocolate', 'Sensacao', 'Menta']
        flavor = 'Limao'
        resultado_esperado = f"Não temos no momento {flavor}!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.find_flavor(flavor)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_find_flavor_sem_estoque(self):
        # Setup
        restaurant_name = 'Delicia_De_Sorvete'
        cuisine_type = 'Sorvete'
        flavors_list = []
        flavor = 'Limao'
        resultado_esperado = "Estamos sem estoque atualmente!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.find_flavor(flavor)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_flavor_ja_disponivel(self):
        # Setup
        restaurant_name = 'Delicia_De_Sorvete'
        cuisine_type = 'Sorvete'
        flavors_list = ['Flocos', 'Morango', 'Chocolate', 'Sensacao', 'Menta']
        flavor = 'Menta'
        resultado_esperado = "Sabor já disponivel!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.add_flavor(flavor)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_flavor_add_estoque(self):
        # Setup
        restaurant_name = 'Delicia_De_Sorvete'
        cuisine_type = 'Sorvete'
        flavors_list = ['Flocos', 'Morango', 'Chocolate', 'Sensacao', 'Menta']
        flavor = 'Maracuja'
        resultado_esperado = f"{flavor} adicionado ao estoque!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.add_flavor(flavor)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_flavor_sem_estoque(self):
        # Setup
        restaurant_name = 'Delicia_De_Sorvete'
        cuisine_type = 'Sorvete'
        flavors_list = []
        flavor = 'Coco'
        resultado_esperado = "Estamos sem estoque atualmente!"
        ice_cream_stand = IceCreamStand(restaurant_name, cuisine_type, flavors_list)

        # Chamada
        resultado = ice_cream_stand.add_flavor(flavor)

        # Avaliacao
        assert resultado_esperado == resultado
