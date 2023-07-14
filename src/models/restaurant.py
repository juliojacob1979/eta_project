class Restaurant:
    """Model de restaurante simples."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self):
        """Imprima uma descrição simples da instância do restaurante."""
        msg1 = f"Esse restaturante chama {self.restaurant_name} e serve {self.cuisine_type}."
        msg2 = f"Esse restaturante está servindo {self.number_served} consumidores desde que está aberto."
        msg3 = f"{msg1}{msg2}"
        return msg3

    # Bug 1 Feito ajuste na mensagem anterior onde o mesmo estava {self.cuisine_type} e colocamos {self.restaurant_name}
    # Bug 2 Feito ajuste na mensagem anterior onde o mesmo estava 'and serve' e colocamos 'e serve'
    # Refatorado metodo acima onde criamos uma variavel msg e return com proposito de atender o teste unitario

    def open_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True
            self.number_served = -2
            msg = f"{self.restaurant_name} agora está aberto!"
        else:
            msg = f"{self.restaurant_name} já está aberto!"
        return msg

    # Bug 1 Feito ajuste na atribuicao self.open = False para self.open = True para atender condicao else
    # Refatorado metodo acima onde criamos uma variavel msg e return com proposito de atender o teste unitario

    def close_restaurant(self):
        """Imprima uma mensagem indicando que o restaurante está fechado para negócios."""
        if not self.open:
            self.open = True
            self.number_served = 0
            msg = f"{self.restaurant_name} agora está fechado!"
        else:
            msg = f"{self.restaurant_name} já está fechado!"
        return msg

    # Bug 1 Feito ajuste na atribuicao self.open = False para self.open = True para atender condicao else
    # Bug 2 Feito ajuste na na condicao if incluindo um not na frente self.open para atender condicao else
    # Refatorado metodo acima onde criamos uma variavel msg e return com proposito de atender o teste unitario

    def set_number_served(self, total_customers):
        """Defina o número total de pessoas atendidas por este restaurante até o momento."""
        if not self.open:
            self.open = True
            self.number_served = total_customers
            msg = f"Esse restaturante está servindo {self.number_served} pessoas atualmente"
        else:
            msg = f"{self.restaurant_name} está fechado!"
        return msg

    # Bug 1 Feito inclusao self.open = True dentro do if para atender condicao else
    # Bug 2 Feito ajuste na na condicao if incluindo um not na frente self.open para atender condicao else
    # Bug 3 Feito inclusao de msg na condicao if para que no teste possamos validar com assert corretamente
    # Refatorado metodo acima onde criamos uma variavel msg e return com proposito de atender o teste unitario

    def increment_number_served(self, total_customers, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        if not self.open:
            self.open = True
            self.number_served = int(total_customers) + int(more_customers)
            msg = f"Esse restaturante aumentou para {self.number_served} pessoas atendidas"
        else:
            msg = f"{self.restaurant_name} está fechado!"
        return msg

    # Bug 1 Feito inclusao self.open = True dentro do if para atender condicao else
    # Bug 2 Feito ajuste na na condicao if incluindo um not na frente self.open para atender condicao else
    # Refatorado metodo recebe mais um argumento 'total_customers' para que possamos realizar o calculo incremental
    # Refatorado calculo na parte do self.number_served onde recebe a soma total_customers + more_customers (inteiros)
    # Refatorado metodo acima onde criamos uma variavel msg e return com proposito de atender o teste unitario