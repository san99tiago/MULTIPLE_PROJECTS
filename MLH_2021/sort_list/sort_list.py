# LIST SORTING USING BUBBLE ALGORITHM
# Santiago Garcia Arango
# MLH2021

class ListSorter:
    def __init__(self, vector, sort_type="numerically", sort_algorithm="bubble"):
        self.vector = vector
        self.sort_type = sort_type

        if sort_algorithm == "bubble":
            self.bubble_sort()

    def bubble_sort(self):
        if self.sort_type == "numerically":
            # Go through the vector as many times as there exists elements
            for i in range(len(self.vector)):
                # Only get to the previous of the last element of list...
                # ... so that we don't run out of index
                for j in range(len(self.vector) - 1):
                    if self.vector[j] > self.vector[j + 1]:
                        # Swap pair of elements when the needs to be sorting
                        temp = self.vector[j]
                        self.vector[j] = self.vector[j + 1]
                        self.vector[j + 1] = temp
            return


if __name__ == "__main__":
    # ---------------- TEST 1 ---------------
    vector = [9, 3, 4, 2, 1, 5, 6, 7, 8]
    print("\n\nORIGINAL: ", vector)
    LS = ListSorter(vector)
    print("SORTED: ", LS.vector)

    # ---------------- TEST 2 ---------------
    vector = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("\n\nORIGINAL: ", vector)
    LS = ListSorter(vector)
    print("SORTED: ", LS.vector)

    # ---------------- TEST 3 ---------------
    vector = [9, 9, 8, 8, 3, 3, 1, 3, 6, 2, 1, 6, 8, 4, 5, 7, 2, 3, 5, 7]
    print("\n\nORIGINAL: ", vector)
    LS = ListSorter(vector)
    print("SORTED: ", LS.vector)
