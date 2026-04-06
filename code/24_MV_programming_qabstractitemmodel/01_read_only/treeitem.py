import json


# 1. Create a tree node class.

class TreeItem:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []
        if parent:
            parent.children.append(self)

    @classmethod
    def build_tree(cls, source):
        root_item = TreeItem("", None)  # Empty root
        with open(source) as json_file:
            data = json.load(json_file)
            for json_object in data:
                name = f"{json_object['firstname']} {json_object['lastname']}"
                tree_item = TreeItem(name, root_item)
                if 'subordinates' in json_object:
                    TreeItem.add_children(json_object, tree_item)
        return root_item

    @staticmethod
    def add_children(json_object, parent):
        for child_json_object in json_object['subordinates']:
            name = f"{child_json_object['firstname']} {child_json_object['lastname']}"
            child = TreeItem(name, parent)
            if 'subordinates' in child_json_object:
                TreeItem.add_children(child_json_object, child)
