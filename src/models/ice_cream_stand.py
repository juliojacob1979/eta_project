from src.models.restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        if self.flavors:
            print("\nNo momento temos os seguintes sabores de sorvete disponíveis:")
            for flavor in self.flavors:
                print(f"\t-{flavor}")
            msg = f"No momento temos os seguintes sabores de sorvete disponíveis: {self.flavors}"
        else:
            msg = "Estamos sem estoque atualmente!"
        return msg
    # Refatorado metodo acima onde criamos uma variavel msg e return com proposito de atender o teste unitario

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        if self.flavors:
            if flavor in self.flavors:
                msg = f"Temos no momento {flavor}!"
            else:
                msg = f"Não temos no momento {flavor}!"
        else:
            msg = "Estamos sem estoque atualmente!"
        return msg
    # Bug 1 Feito ajuste na mensagem anterior onde o mesmo estava {self.flavors} e colocamos {flavor}
    # Refatorado metodo acima onde criamos uma variavel msg e return com proposito de atender o teste unitario

    def add_flavor(self, flavor):
        """Add o sabor informado ao estoque."""
        if self.flavors:
            if flavor in self.flavors:
                msg = "Sabor já disponivel!"
            else:
                self.flavors.append(flavor)
                msg = f"{flavor} adicionado ao estoque!"
        else:
            msg = "Estamos sem estoque atualmente!"
        return msg
    # Refatorado metodo acima onde criamos uma variavel msg e return com proposito de atender o teste unitario
