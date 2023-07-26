# ws_7_4.py

# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # self.area = self.calculate_area()
        # self.perimeter = self.calculate_perimeter()
        # 이게 실행되는 이유는 width와 height가 더 위에 있고,
        # 순차적으로 실행했을 때 연산이 가능한 순서이므로!

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return (self.width + self.height) * 2
    
    # def print_info(self):
    #     print(f'Width: {self.width}')
    #     print(f'Height: {self.height}')
    #     print(f'Area: {self.area}')
    #     print(f'Permiter: {self.perimeter}')    

    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.calculate_area()}')
        print(f'Permiter: {self.calculate_perimeter()}')
        # self.메서드() 를 바로 삽입하는 것도 가능!!


shape1 = Shape(5, 3)
shape1.print_info()
