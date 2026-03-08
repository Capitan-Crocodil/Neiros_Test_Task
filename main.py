import math

class Point:
    def __init__(self, x:float, y:float):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Точка ({self.__x}, {self.__y})"
    
    def move(self, new_x: float, new_y:float):
        self.__x = new_x
        self.__y = new_y

    def get_x(self):
        return self.__x
    
    def get_y(self):
        return self.__y
    
    def set_x(self, x):
        self.__x = x
    
    def set_y(self, y):
        self.__y = y
        
    
class Segment:
    def __init__(self, start: Point, end:Point):
        self.__start = start
        self.__end = end
    
    def __str__(self):
        return f"Отрезок [({self.__start.get_x()}, {self.__start.get_y()}) -> ({self.__end.get_x()}, {self.__end.get_y()})]"

    def move(self, start_x: float, start_y: float, end_x: float, end_y: float):
        self.__start.move(start_x, start_y)
        self.__end.move(end_x, end_y)

    def length(self):
        return math.sqrt((self.__end.get_x() - self.__start.get_x())**2 + 
                         (self.__end.get_y() - self.__start.get_y())**2)
    
    def get_start(self):
        return self.__start
    
    def get_end(self):
        return self.__end

class Circle:
    def __init__(self, centre: Point, radius: float):
        self.__centre = centre
        self.__radius = radius
    
    def __str__(self):
        return f"Круг (центр: ({self.__centre.get_x()}, {self.__centre.get_y()}), радиус: {self.__radius})"

    def move(self, new_x: float, new_y: float, new_radius: float):
        self.__centre.move(new_x, new_y)
        self.__radius = new_radius

    def get_centre(self):
        return self.__centre
    
    def get_radius(self):
        return self.__radius

class Square:
    def __init__(self, top_left: Point, side_length: float):
        self.__top_left = top_left
        self.__side_length = side_length
        self.__top_right = Point(top_left.get_x() + side_length, top_left.get_y())
        self.__bottom_left = Point(top_left.get_x(), top_left.get_y() + side_length)
        self.__bottom_right = Point(top_left.get_x() + side_length, top_left.get_y() + side_length)
     
    def __str__(self):
        return (f"Квадрат (Левая верхняя: ({self.__top_left.get_x()}, {self.__top_left.get_y()}), "
                f"Правая верхняя: ({self.__top_right.get_x()}, {self.__top_right.get_y()}), "
                f"Левая нижняя: ({self.__bottom_left.get_x()}, {self.__bottom_left.get_y()}), "
                f"Правая нижняя: ({self.__bottom_right.get_x()}, {self.__bottom_right.get_y()})), "
                f"длина стороны: {self.__side_length})")

    def move(self, new_top_left_x: float, new_top_left_y: float):
        self.__top_left.move(new_top_left_x, new_top_left_y)
        self.__top_right.move(new_top_left_x + self.__side_length, new_top_left_y)
        self.__bottom_left.move(new_top_left_x, new_top_left_y + self.__side_length)
        self.__bottom_right.move(new_top_left_x + self.__side_length, new_top_left_y + self.__side_length)
    
    def get_top_left(self):
        return self.__top_left
    
    def get_side_length(self):
        return self.__side_length
    

class VectorEditor:
    def __init__(self):
        self.shapes = []
        self.shapes_counter = 0

    def add_shape(self, shape_type, *args):
        self.shapes_counter += 1
        shape_id = self.shapes_counter

        try:
            if shape_type == 'point':
                if len(args) == 2:
                    shape = Point(float(args[0]), float(args[1]))
                    self.shapes.append((shape_id, "Точка", shape))
                    print(f"Создана точка с ID {shape_id}")
                else:
                    self.shapes_counter -= 1
                    raise Exception("Ошибка: неверный формат или количество входных данных, " \
                    "для точки нужны координаты x и y")
            
            elif shape_type == 'segment':
                if len(args) == 4:
                    start = Point(float(args[0]), float(args[1]))
                    end = Point(float(args[2]), float(args[3]))
                    shape = Segment(start, end)
                    self.shapes.append((shape_id, "Отрезок", shape))
                    print(f"Создан отрезок с ID {shape_id}")
                else: 
                    self.shapes_counter -= 1
                    raise Exception("Ошибка: неверный формат или количество входных данных, " \
                    "для отрезка нужны координаты начала (x1,y1) и конца (x2,y2)")
                
            elif shape_type == 'circle':
                if len(args) == 3:
                    centre = Point(float(args[0]), float(args[1]))
                    shape = Circle(centre, float(args[2]))
                    self.shapes.append((shape_id, "Круг", shape))
                    print(f"Создан круг с ID {shape_id}")
                else: 
                    self.shapes_counter -= 1
                    raise Exception("Ошибка: неверный формат или количество входных данных, " \
                    "для круга нужны координаты центра (x,y) и радиус")
                
            elif shape_type == "square":
                if len(args) == 3:
                    top_left = Point(float(args[0]), float(args[1]))
                    shape = Square(top_left, float(args[2]))
                    self.shapes.append((shape_id, "Квадрат", shape))
                    print(f"Создан квадрат с ID {shape_id}")
                else: 
                    self.shapes_counter -= 1
                    raise Exception("Ошибка: неверный формат или количество входных данных, " \
                    "для квадрата нужны координаты левого верхнего угла (x,y) и длина стороны")
            
            else: 
                self.shapes_counter -= 1
                raise Exception("Ошибка: неизвестный тип фигуры")
            
        except ValueError:
            print("Ошибка: неверный формат чисел")
            self.shapes_counter_counter -= 1

    def remove(self, shape_id):
        for i, (id, stype, shape) in enumerate(self.shapes):
            if id == shape_id:
                del self.shapes[i]
                print(f"Удалена фигура с ID {shape_id}")
                return
        raise Exception(f"Ошибка: фигура с ID {shape_id} не найдена")
    
    def print_shapes(self):
        if len(self.shapes) == 0:
            print("Список фигур пуст")
            return
        print("Список фигур")
        for id, stype, shape in self.shapes:
            print(f"ID: {id}, Тип: {stype}, Фигура: {shape}")

    def move_figure(self, shape_id, *args):
        for id, stype, shape in self.shapes:
            if id == shape_id:
                try:
                    if stype == "Точка":
                        if len(args) == 2:
                            shape.move(float(args[0]), float(args[1]))
                            print(f"Точка {shape_id} перемещена")
                        else:
                            Exception("Ошибка: нужны новые координаты x, y")

                    elif stype == "Отрезок":
                        if len(args) == 4:
                            shape.move(float(args[0]), float(args[1]), 
                                      float(args[2]), float(args[3]))
                            print(f"Отрезок {shape_id} перемещен")
                        else:
                            Exception("Ошибка: нужны координаты начала (x1,y1) и конца (x2,y2)")

                    elif stype == "Круг":
                        if len(args) == 3:
                            shape.move(float(args[0]), float(args[1]), float(args[2]))
                            print(f"Круг {shape_id} перемещен")
                        else:
                            Exception("Ошибка: нужны новые координаты центра (x,y) и радиус")

                    elif stype == "Квадрат":
                        if len(args) == 2:
                            shape.move(float(args[0]), float(args[1]))
                            print(f"Квадрат {shape_id} перемещен")
                        else:
                            Exception("Ошибка: нужны новые координаты левого верхнего угла (x,y)")

                    return
                except ValueError:
                    print("Ошибка: неверный формат чисел")
                    return
        
        print(f"Ошибка: фигура с ID {shape_id} не найдена")
    
    def run(self):
        print("Доступные команды:")
        print("  add <тип> <параметры> - добавить фигуру")
        print("  типы: point (x y), segment (x1 y1 x2 y2), circle (x y r), square (x y side), remove <id> - удалить фигуру")
        print("  list - показать все фигуры")
        print("  move <id> <параметры> - переместить фигуру")
        print("  help - показать справку")
        print("  exit - выход")
        print()
        
        while True:
            try:
                command = input("> ").strip().lower()
                
                if not command:
                    continue
                
                parts = command.split()
                cmd = parts[0]
                
                if cmd == "exit":
                    print("До свидания!")
                    break
                
                elif cmd == "help":
                    print("Доступные команды:")
                    print("  add point <x> <y>")
                    print("  add segment <x1> <y1> <x2> <y2>")
                    print("  add circle <x> <y> <radius>")
                    print("  add square <x> <y> <side_length>")
                    print("  remove <id>")
                    print("  list")
                    print("  move <id> <параметры> (зависят от типа фигуры)")
                    print("  exit")
                
                elif cmd == "add":
                    if len(parts) < 2:
                        print("Ошибка: укажите тип фигуры")
                        continue
                    
                    shape_type = parts[1]
                    params = parts[2:] if len(parts) > 2 else []
                    self.add_shape(shape_type, *params)
                
                elif cmd == "remove":
                    if len(parts) < 2:
                        print("Ошибка: укажите ID фигуры")
                        continue
                    
                    try:
                        shape_id = int(parts[1])
                        self.remove(shape_id)
                    except ValueError:
                        print("Ошибка: ID должен быть числом")
                
                elif cmd == "list":
                    self.print_shapes()
                
                elif cmd == "move":
                    if len(parts) < 2:
                        print("Ошибка: укажите ID фигуры")
                        continue
                    
                    try:
                        shape_id = int(parts[1])
                        params = parts[2:] if len(parts) > 2 else []
                        self.move_figure(shape_id, *params)
                    except ValueError:
                        print("Ошибка: ID должен быть числом")
                
                else:
                    print(f"Неизвестная команда: {cmd}")
                    print("Введите 'help' для списка команд")
                    
            except KeyboardInterrupt:
                print("\nДо свидания!")
                break
            except Exception as e:
                print(f"Ошибка: {e}")    
    
if __name__ == "__main__":
    editor = VectorEditor()
    editor.run()