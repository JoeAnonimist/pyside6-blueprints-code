import json


# 1. Implement the tree node class

class TreeItem:
    
    COLUMNS = ['name', 'budget', 'actual']

    def __init__(self, data=None, parent=None):
        
        if data is not None:
            self.item_data = data
        else:
            self.item_data = [''] * len(TreeItem.COLUMNS)

        self.parent = parent
        self.children = []

        if parent:
            self.parent.append_child(self)
            
    def append_child(self, item):
        self.children.append(item)
        
    def child(self, row):
        return self.children[row]
    
    def child_count(self):
        return len(self.children)
    
    def column_count(self):
        return len(self.item_data)
    
    def data(self, column):
        try:
            return self.item_data[column]
        except IndexError:
            return None
        
    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        else:
            return 0
            
    @classmethod
    def build_tree(cls, source):
        
        root_item = TreeItem(parent=None)
        
        with open(source) as json_file:
            data = json.load(json_file)
            for json_object in data:
                tree_item = TreeItem.create_item(
                    json_object, root_item)
                if 'children' in json_object:
                    TreeItem.add_children(json_object, tree_item)
                    
        return root_item
    
    @staticmethod
    def add_children(json_object, parent):
        for child_json_object in json_object['children']:
            child = TreeItem.create_item(
                child_json_object, parent)
            if 'children' in child_json_object:
                TreeItem.add_children(child_json_object, child)

    @staticmethod
    def create_item(json_object, parent):
        data = [json_object.get(col) for col in TreeItem.COLUMNS]
        return TreeItem(data, parent)
    