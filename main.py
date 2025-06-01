import tkinter as tk
from tkinter import messagebox, scrolledtext

def FindTheLongestCycle(graph):
    """
    Finds the longest cycle in a directed graph represented by an adjacency matrix.
    """
    def dfs(node, visited, rec_stack, path, max_cycle_ref):
        visited[node] = True
        rec_stack[node] = True
        path.append(node)

        for neighbor in range(len(graph)):
            if graph[node][neighbor] == 1:
                if not visited[neighbor]:
                    dfs(neighbor, visited, rec_stack, path, max_cycle_ref)
                elif rec_stack[neighbor]:
                    try:
                        cycle_start_index = path.index(neighbor)
                        current_cycle = path[cycle_start_index:]
                        if len(current_cycle) > len(max_cycle_ref[0]):
                            max_cycle_ref[0] = current_cycle.copy()
                    except ValueError:
                        pass


        rec_stack[node] = False
        path.pop()

    n = len(graph)
    if n == 0:
        return [] 

    visited = [False] * n
    rec_stack = [False] * n
    max_cycle_ref = [[]]

    for node in range(n):
        if not visited[node]:
            dfs(node, visited, rec_stack, [], max_cycle_ref)

    return max_cycle_ref[0]

class GraphGUI:
    def __init__(self, master):
        self.master = master
        master.title("Znajdowanie najdłuższego cyklu w grafie 🔄")

        self.label_instruction = tk.Label(master, text="Wprowadź macierz sąsiedztwa (zera i jedynki):\nRzędy oddzielone nowymi liniami, wartości przez spacje lub przecinki.")
        self.label_instruction.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(master, width=40, height=10, wrap=tk.WORD)
        self.text_area.pack(pady=10, padx=10)
        self.text_area.insert(tk.INSERT, "0 1 0 0\n0 0 1 0\n0 0 0 1\n1 0 0 0")

        self.find_button = tk.Button(master, text="Find Longest Cycle", command=self.process_matrix)
        self.find_button.pack(pady=10)

    def parse_matrix(self, matrix_str):
        """ Parses the string input into a 2D list of integers (adjacency matrix). """
        graph = []
        lines = matrix_str.strip().split('\n')
        num_cols = -1
        for i, line in enumerate(lines):
            try:
                row_str = line.replace(',', ' ').split()
                row_int = [int(val) for val in row_str if val]
                if not row_int and not lines:
                    continue
                if not row_int and lines:
                     raise ValueError(f"Rząd {i+1} jest pusty lub zawiera niepoprawne znaki.")


                if not all(val in (0, 1) for val in row_int):
                    raise ValueError(f"Wartości macierzy musza być równe zero lub jeden. Znaleziono nieprawidłową wartość w rzędzie: {i+1}.")

                if i == 0:
                    num_cols = len(row_int)
                elif len(row_int) != num_cols:
                    raise ValueError(f"Macierz nie jest kwadratowa. Rząd {i+1} ma {len(row_int)} elementów, spodziewane: {num_cols}.")

                graph.append(row_int)
            except ValueError as e:
                raise ValueError(f"Wystąpił błąd w rzędzie: {i+1}: {e}")

        if not graph:
            raise ValueError("Input matrix is empty.")

        if len(graph) != num_cols and num_cols != -1 :
             raise ValueError(f"Macierz przystawania musi być kwadratowa. Otrzymano {len(graph)} rzędów oraz {num_cols} kolumn.")

        return graph

    def process_matrix(self):
        matrix_str = self.text_area.get("1.0", tk.END)
        try:
            graph = self.parse_matrix(matrix_str)
            if not graph:
                messagebox.showerror("Błąd", "Macierz jest niepoprawna.")
                return

            longest_cycle = FindTheLongestCycle(graph)

            if longest_cycle:
                cycle_display = longest_cycle
                result_message = f"Znaleziono najdłuższy cykl: {' -> '.join(map(str, cycle_display))}"
                if len(cycle_display) > 0:
                    result_message += f" -> {cycle_display[0]}"
                result_message += f"\nDługość: {len(longest_cycle)}"
            else:
                result_message = "Brak cyklu w grafie."

            messagebox.showinfo("Wynik działania algorytmu 📊", result_message)

        except ValueError as e:
            messagebox.showerror("Wprowadzono błędną wartość: ❌", str(e))
        except Exception as e:
            messagebox.showerror("Błąd ⚠️", f"Niespodziewany błąd: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = GraphGUI(root)
    root.mainloop()