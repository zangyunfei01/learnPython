class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth



class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,height):
        self._height = height

    @property
    def resolution(self):
        return self.width*self.height