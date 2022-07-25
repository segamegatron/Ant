# python: 3.7


class Ant:

    def __init__(self, start_x: int, start_y: int, step: int, constraint: int):
        self.start_x: int = start_x
        self.start_y: int = start_y
        self.step: int = step
        self.point: list = [self.start_x, self.start_y]
        self.constraint: int = constraint
        self.steps: int = 1
        self.dct: list = [[self.start_x, self.start_y], step, constraint]

    def __str__(self) -> str:
        start_elements: str = ""
        for start_element in self.dct:
            start_elements += str(start_element) + ", "
        return "Муравей создан с такими начальными значениями -> координаты [x, y], шаг, ограничение соответственно" \
               "-> " + start_elements[:-2]

    def in_bound(self) -> bool:
        return self.sum_point(self.point[0]) + self.sum_point(self.point[1]) <= self.constraint

    def all_points(self):
        while self.in_bound():
            self.point[0] += self.step
            if self.in_bound():
                self.steps += self.step
                # print(self.point)
            else:
                self.point[0] = self.start_x
                self.point[1] += self.step
                if self.in_bound():
                    self.steps += self.step
                    # print(self.point)

    @staticmethod
    def sum_point(point: int) -> int:
        nums: list = list(str(point))
        all_nums: int = 0
        for num in nums:
            all_nums += int(num)
        return all_nums

    @staticmethod
    def get_length_point(point: int) -> int:
        s_point: str = str(point)
        return len(s_point)


if __name__ == "__main__":
    # ant: Ant = Ant(1000, 1000, 1, 5)
    ant: Ant = Ant(1000, 1000, 1, 25)
    print(ant.__str__())
    ant.all_points()  # считаем все шаги
    print(f"всего муравей посетил -> {ant.steps} клеток")
