class CashBox:
    def __init__(self):
        self.balance = 0 # Начальное к-во денег

    def top_up(self, amount):
        """Пополнение кассы"""
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Сумма пополнения должна быть положительной")
        
    def count_1000(self):
        """Подсчет количества тысяч"""
        return self.balans // 1000
    
    def take_away(self, amount):
        """Cнятие денег из кассы"""
        if amount > self.balance:
            raise ValueError("Недостаточно средств в кассе")
        if amount < 0:
            raise ValueError("Сумма снятия должна быть положителой")
        self.balance -= amount