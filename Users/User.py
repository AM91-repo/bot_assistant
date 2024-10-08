import sys
if __name__ == '__main__': sys.path.append('../')

from DataBase.DB import DBHandler


class HandlerUser():
    def __init__(self, name='0') -> None:
        self.name = name

    def get_name(self):
        return self.name
    
    def hadler_message(self, message=''):
        pass

    def answer_massage(self):
        pass


if __name__ == "__main__":
    pass
