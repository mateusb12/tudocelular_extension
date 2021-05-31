class Smartphone:
    def __init__(self, name, image, price, store, tudocelular_store, camera_grade, performance_grade, battery_grade):
        self.name = name
        self.image = image
        self.price = price
        self.store = store
        self.tudocelular_store = tudocelular_store
        self.camera_grade = camera_grade
        self.performance_grade = performance_grade
        self.battery_grade = battery_grade

    def __str__(self):
        return '{' \
               f'name: {self.name}, ' \
               f'image: {self.image}, ' \
               f'price: {self.price}, ' \
               f'store: {self.store}, ' \
               f'tudocelular_store: {self.tudocelular_store}, ' \
               f'camera_grade: {self.camera_grade}, ' \
               f'performance_grade: {self.performance_grade}, ' \
               f'battery_grade: {self.battery_grade}' \
               '}'
