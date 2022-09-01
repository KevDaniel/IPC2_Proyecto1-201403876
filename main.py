from os import system, startfile
import xml.etree.ElementTree as ET


class Patient:
    def __init__(self, name, age, size):
        self.name = name
        self.age = age
        self.size = size


class Node:
    def __init__(self, patient=None, next_position=None):
        self.patient = patient
        self.next_position = next_position


class LinkedList:
    def __init__(self):
        self.first = None

    def insert(self, patient):
        if self.first is None:  # For first insert, it will just verify if first position is empty
            self.first = Node(patient=patient)
            return
        actual = self.first
        while actual.next_position:  # While actual.first is not empty it will keep running.
            actual = actual.next_position
        actual.next_position = Node(patient=patient)

    def run(self):
        actual = self.first
        while actual is not None:
            print("|Paciente:", actual.patient.name, "|Edad:", actual.patient.age, "|Tamaño:", actual.patient.size)
            actual = actual.next_position

    def delete(self, name):
        actual = self.first
        previous = None

        while actual and actual.patient.name != name:
            previous = actual
            actual = actual.next_position

        if previous is None:
            self.first = actual.next_position
            actual.next_position = None
        elif actual:
            previous.next_position = actual.next_position
            actual.next_position = None

    def search(self, name):
        actual = self.first

        while actual and actual.patient.name != name:
            actual = actual.next_position
        print("|Paciente:", actual.patient.name, "|Edad:", actual.patient.age, "|Tamaño:", actual.patient.size)


def draw_list():
    graphviz = """
    digraph myGraph{
    node[shape=box fillcolor="#FFEDBB" style=filled]
    subgraph cluster_p{
        label = "Matriz Dispersa"
        bgcolor = "#398D9C"
        edge[dir = "none"]
        /*Here we start creating the columns.
        color = "#398D9C" style=invisible
        */
        Row1[label="r1"]
        Row2[label="r2"]
        Row3[label="r3"]
        Row4[label="r4"]
        Row5[label="r5"]
        Row6[label="r6"]
        Row7[label="r7"]

        Row1 -> Row2;


        Fila1[label="1", group=1];
        Fila2[label="2", group=2];
        Fila3[label="3", group=3];
        Fila4[label="4", group=4];
        Fila5[label="5", group=5];
        /*Linkin the nodes*/
        Fila1 -> Fila2;
        Fila2 -> Fila3;
        Fila3 -> Fila4;
        Fila4 -> Fila5;
        /*Enlazando los nodos de las filas.*/
        Columna1[label = "1", group = 2, fillcolor=yellow]
        Columna2[label = "2", group = 3, fillcolor=yellow]
        Columna3[label = "3", group = 4, fillcolor=yellow]
        Columna4[label = "4", group = 5, fillcolor=yellow]
        Columna5[label = "5", group = 6, fillcolor=yellow]
        /*Enlazando los nodos de las columnas.*/
        Columna1 -> Columna2
        Columna2 -> Columna3
        Columna3 -> Columna4
        Columna4 -> Columna5
    }
}  
    """
    my_file = open("graphviz.dot", "w")
    my_file.write(graphviz)
    my_file.close()

    system("dot -Tpng graphviz.dot -o graphviz.png")  # Generates the png picture.
    startfile("graphviz.png")


def fn_read_xml():
    try:
        file_xml = open("Example.xml")
        if file_xml.readable():
            data_xml = ET.fromstring(file_xml.read())
            patient_list = data_xml.findall("paciente")
            print("\nLectura de XML")
            for element in patient_list:
                print("")
                print(f"Edad: {element.find('datospersonales').find('nombre').text}")
                print(f"Edad: {element.find('datospersonales').find('edad').text}")
                print(f"Periodos: {element.find('periodos').text}")
                print(f"Valor de M: {element.find('m').text}")
                cell_list = element.find('rejilla').findall('celda')
                for i in range(len(cell_list)):
                    print(f"Valor de F: {cell_list[i].get('f')} Valor de C: {cell_list[i].get('c')}")
        file_xml.close()
    except Exception as err:
        print("Error:", err)


p1 = Patient("Kevin", 28, 10)
p2 = Patient("Marielena", 38, 30)
p3 = Patient("Sykkuno", 23, 140)
p4 = Patient("Leslie", 32, 110)
p5 = Patient("Rachel", 30, 520)
p6 = Patient("Miyoung", 29, 50)

linked_l = LinkedList()
linked_l.insert(p1)
linked_l.insert(p2)
linked_l.insert(p3)
linked_l.insert(p4)
linked_l.insert(p5)
linked_l.insert(p6)

print("Recorriendo la Lista")
linked_l.run()

print("\nBuscando un elemento en la lista.")
linked_l.search("Rachel")

print("\nDespues de eliminar registro")
linked_l.delete("Leslie")
linked_l.run()
# Function that draws the list visually. draw_list()
fn_read_xml()
