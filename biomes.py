from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QVBoxLayout, QLabel, QWidget, QLineEdit, QPushButton

show_file = r"./data/rpgtitles/functions/titles/biome/show.mcfunction"
namespace_file = r"./data/rpgtitles/functions/titles/biome/NAMESPACE.mcfunction"
predicate_folder = r"./data/rpgtitles/predicates/entity/player/in_biome/NAMESPACE/BIOME_ID.json"

colors = {
    "minecraft": "green",
    "terralith": "aqua",
    "tectonic": "light_purple"
}

command_template = 'execute if predicate rpgtitles:entity/player/in_biome/NAMESPACE/BIOME_ID run title @s actionbar {"text":"Biome: BIOME_NAME","color": "UCOLOR"}'
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
        self.biome_input.setPlaceholderText("Default: \"biome_id\"")
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
        namespace = self.namespace_input.text()
        biome_name = self.biome_input.text()
        biome_id = self.biomeid_input.text()
        if namespace == "":
            namespace = "minecraft"

        if biome_name == "":
            biome_name = biome_id.replace("_", " ").title()

        if biome_id != "":
            predicate = predicate_template
            namespaced_biome_id = f"\"{namespace}:{biome_id}\""
            predicate = predicate.replace("BIOME_ID", namespaced_biome_id)

            predicate_path = predicate_folder
            predicate_path = predicate_path.replace("NAMESPACE", namespace)
            predicate_path = predicate_path.replace("BIOME_ID", biome_id)

            command = command_template
            command = command.replace("NAMESPACE", namespace)
            command = command.replace("BIOME_ID", biome_id)
            command = command.replace("BIOME_NAME", biome_name)
            command = command.replace("UCOLOR", colors[namespace])

            unique_command_file = namespace_file
            unique_command_file = unique_command_file.replace("NAMESPACE", namespace)
            
            print(predicate)
            print(predicate_path)
            print(command)
            print(unique_command_file)
            
            with open(unique_command_file, "a") as f:
                f.write("\n"+command)
            with open(predicate_path, "a") as f:
                f.write("\n"+predicate)
            with open("./temp_preds.txt", "a") as f:
                f.write(",\n"+predicate)

        # if bn != "" and bid != "":
        #     pred = predicate_template
        #     strbid = f'"{ns}:{bid}"'
        #     pred = pred.replace("BIOME_ID", strbid)
        #     pred_path = pred_folder
        #     pred_path = pred_path.replace("BIOME_ID", bid)

        #     comm = command_template
        #     comm = comm.replace("BIOME_ID", bid)
        #     comm = comm.replace("BIOME_NAME", bn)

        #     with open(show_file, "a") as f:
        #         f.write("\n"+comm)

        #     with open(pred_path, "w") as f:
        #         f.write(pred)
        # else:
        #     print(ns, "bn and bid have to be set")


app = QApplication()
window = MainWindow()
app.exec()