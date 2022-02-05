class SortingAlgo:
    def __init__(self):
        pass
        
    def bubble_sort(self, draw_info, draw_list, ascending=True):
        self.lst = draw_info.lst

        for i in range(len(self.lst)-1):
            for j in range(len(self.lst) - 1 - i):
                num1 = self.lst[j]
                num2 = self.lst[j + 1]

                if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                    self.lst[j], self.lst[j + 1] = self.lst[j + 1], self.lst[j]
                    draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
                    yield True
        print(self.lst)
        return self.lst

    def insertion_sort(self, draw_info, draw_list, ascending=True):
        self.lst = draw_info.lst

        for i in range(1, len(self.lst)):
            self.current = self.lst[i]

            while True:
                self.ascending_sort = i > 0 and self.lst[i - 1] > current and ascending
                self.descending_sort = i > 0 and self.lst[i - 1] < current and not ascending

                if not self.ascending_sort and not self.descending_sort:
                    break

                self.lst[i] = self.lst[i - 1]
                i = i - 1
                self.lst[i] = self.current
                draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
                yield True

        return self.lst
