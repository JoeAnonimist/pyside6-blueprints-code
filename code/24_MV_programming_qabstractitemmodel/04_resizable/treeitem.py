import json


# 1. Add a class-level `counter` to `TreeItem`
#    to assign unique IDs to newly inserted nodes.

class TreeItem:
    
    COLUMNS = ['name', 'budget', 'actual']
    counter = 0

    def __init__(self, data=None, parent=None):
        
        if data is not None:
            self.item_data = data
        else:
            self.item_data = [''] * len(TreeItem.COLUMNS)

        self.parent = parent
        self.children = []

    def append_child(self, item):
        TreeItem.counter += 1
        self.children.append(item)
        
    def child(self, row):
        if self.child_count() > row:
            return self.children[row]
        else:
            return None
    
    def child_count(self):
        return len(self.children)
    
    def column_count(self):
        return len(self.item_data)
    
    def data(self, column):
        try:
            return self.item_data[column]
        except IndexError:
            return None
    
    def set_data(self, column, value):
        self.item_data[column] = value
        
    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        else:
            return 0
    
    # 2. Add methods to insert and remove a child node.
    
    def insert_child(self, row):
        TreeItem.counter += 1
        data = [f'New Item {TreeItem.counter}', '', '']
        item = TreeItem(data, self)
        self.children.insert(row, item)
            
    def remove_child(self, row):
        self.children[row:row + 1] = []
            
    @staticmethod
    def build_tree(source):
        
        root_item = TreeItem(parent=None)
        
        with open(source) as json_file:
            data = json.load(json_file)
            for json_object in data:
                tree_item = TreeItem.create_item(
                    json_object, root_item)
                root_item.append_child(tree_item)
                if 'children' in json_object:
                    TreeItem.add_children(json_object, tree_item)
                    
        return root_item
    
    @staticmethod
    def add_children(json_object, parent):
        for child_json_object in json_object['children']:
            child = TreeItem.create_item(
                child_json_object, parent)
            parent.append_child(child)
            if 'children' in child_json_object:
                TreeItem.add_children(child_json_object, child)
    
    @staticmethod
    def create_item(json_object, parent):
        data = [json_object.get(col) for col in TreeItem.COLUMNS]
        return TreeItem(data, parent)
