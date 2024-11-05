class UtilView:

    view = None

    @staticmethod
    def instance():
        if UtilView.view is None:
            UtilView.view = UtilView()
        return UtilView.view

    def show_deco(self, size: int, deco: chr = '-', step = 0):
        for index in range(size):
            m_deco = deco
            if step % 2 == 1 and index % 2 == 1: m_deco = " "
            end = ""
            if index == size - 1:
                end = "\n" 
            print(m_deco, end= end)

    def show_line(self, size: int, deco: chr = '-'):
        for _ in range(size):
            print(deco, end= "")
        print()


    def show_border(self, message: str, deco: chr = "-"):
        size = len(message)
        self.show_line(size=size, deco=deco)
        print(message)
        self.show_line(size=size, deco=deco)