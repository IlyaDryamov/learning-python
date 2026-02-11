class Turtle:
    def __init__(self, x=0, y=0, step=1):
        self.x = x
        self.y = y
        self.s = step #Размер шага

    def go_up(self):
        '''Движение вверх'''
        self.y += self.s

    def go_down(self):
        '''Движение вниз'''
        self.y -=self.s

    def go_left(self):
        '''Движение влево'''
        self.x -= self.s

    def go_right(self):
        '''Движение в право'''
        self.x += self.s

    def evolve(self):
        '''Увеличение шага'''
        self.s += 1

    def degrade(self):
        '''Уменьшение шага'''
        if self.s > 1:
            self.s -= 1
        else:
            raise ValueError('Шаг не может быть меньше 1')

    def count_moves(self, x2, y2):
        '''Расчет минимального количества ходов'''
        dx = abs(x2 - self.x)
        dy = sbs(y2 - self.y)
        return (dx + dy + self.s -1) // self.s # округление в верх
    
# Пример использования:
# черепашка = Turtlle(0, 0, 2)
# черепашка.go_right()
# черепашка.evolve()
# print(черепашка.count_moves(5, 5))  \ расчет до точки (5, 5)