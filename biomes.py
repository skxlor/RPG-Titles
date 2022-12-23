from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QLineEdit, QPushButton

show_file = r"./data/rpgtitles/functions/titles/biome/show.mcfunction"
pred_folder = r"./data/rpgtitles/predicates/entity/player/in_biome/terralith/BIOME_ID.json"

command_template = 'execute if predicate rpgtitles:entity/player/in_biome/terralith/BIOME_ID run title @s actionbar {"text":"Biome: BIOME_NAME","color": "aqua"}'
predicate_template = '''{
    "condition": "minecraft:entity_properties",
    "entity": "this",
    "predicate": {
        "location": {
            "biome": BIOME_ID
        }
    }
}'''


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()

        self.setWindowTitle("Biome Title Helper")
        self.setFixedWidth(400)
        self.setFixedHeight(125)

        lay = QVBoxLayout()
        lay.setAlignment(Qt.AlignmentFlag.AlignTop)

        namespace = QHBoxLayout()
        namespace_label = QLabel("Namespace:")
        namespace_label.setMinimumWidth(75)
        namespace.addWidget(namespace_label)
        self.namespace_input = QLineEdit()
        self.namespace_input.setPlaceholderText("Default: \"minecraft\"")
        namespace.addWidget(self.namespace_input)

        biome = QHBoxLayout()
        biome_label = QLabel("Biome Name:")
        biome_label.setMinimumWidth(75)
        biome.addWidget(biome_label)
        self.biome_input = QLineEdit()
        self.biome_input.setPlaceholderText("e.g. \"Birch Forest\"")
        biome.addWidget(self.biome_input)

        biomeid = QHBoxLayout()
        biomeid_label = QLabel("Biome ID:")
        biomeid_label.setMinimumWidth(75)
        biomeid.addWidget(biomeid_label)
        self.biomeid_input = QLineEdit()
        self.biomeid_input.setPlaceholderText("e.g. \"birch_forest\"")
        biomeid.addWidget(self.biomeid_input)

        save = QPushButton("Save..")
        save.clicked.connect(self.saveButton)

        lay.addLayout(namespace)
        lay.addLayout(biome)
        lay.addLayout(biomeid)
        lay.addWidget(save)
        widget = QWidget()
        widget.setLayout(lay)

        self.setCentralWidget(widget)

        self.show()

    def saveButton(self):
        ns = self.namespace_input.text()
        bn = self.biome_input.text()
        bid = self.biomeid_input.text()
        if ns == "":
            ns = "minecraft"
        if bn != "" and bid != "":
            pred = predicate_template
            strbid = f'"{ns}:{bid}"'
            pred = pred.replace("BIOME_ID", strbid)
            pred_path = pred_folder
            pred_path = pred_path.replace("BIOME_ID", bid)

            comm = command_template
            comm = comm.replace("BIOME_ID", bid)
            comm = comm.replace("BIOME_NAME", bn)

            with open(show_file, "a") as f:
                f.write("\n"+comm)

            with open(pred_path, "w") as f:
                f.write(pred)
        else:
            print(ns, "bn and bid have to be set")


app = QApplication()
window = MainWindow()
app.exec()