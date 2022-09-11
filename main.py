import datetime


class Node:
    def __init__(self, item, objects) -> None:
        self.left = None
        self.right = None
        self.data = item
        self.dict = objects


class BinaryTree:

    def __init__(self):
        self.round_up_count = 0

    def insert(self, root, item, objects):
        if root is None:
            self.round_up_count += 1
            return Node(item, objects)

        if root.data > item:
            root.left = self.insert(root.left, item, objects)
        else:
            root.right = self.insert(root.right, item, objects)

        return root

    def inorderSequence(self, root):
        if root is None:
            return
        self.inorderSequence(root.left)
        print(root.dict, root.data)
        self.inorderSequence(root.right)

    def removeNode(self, root, item):
        if root is None:
            return None

        if root.data > item:
            root.left = self.removeNode(root.left, item)
        elif root.data == item:
            # case 1

            if root.left is None and root.right is None:
                return None
            # case 2
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # case 2 throw children
            inorder_successer = self.inroderSuccesser(root.right)

            root.value = inorder_successer.data
            root.right = self.removeNode(root.right, inorder_successer.data)

        else:
            root.right = self.removeNode(root.right, item)

        return root

    def inroderSuccesser(self, root):
        while True:
            if root.left is None:
                break
            else:
                root = root.left

        return root

    def makeSearch(self, root, item):

        class People:
            def __init__(self):
                self.valid_node = None

            def make_search(self, base, item):
                if base is None:
                    return
                self.make_search(base.left, item)
                node = base.dict
                if node is not None:
                    status = node["active"]
                    if status and base.data != item:
                        node["active"] = False
                        node["requested"] = item
                        self.valid_node = base
                        return base
                self.make_search(base.right, item)

            def get_result(self):
                return self.valid_node

        init = People()
        init.make_search(root, item)
        return init.get_result()

    def searching_user_requested_node(self, root, item):

        class Peoples:
            def __init__(self):
                self.value = None

            def make_search(self, base, items):
                if base is None:
                    return
                self.make_search(base.left, items)
                node = base.dict
                if node is not None:
                    request = node["requested"]
                    if request == items:
                        self.value = node
                        return node
                self.make_search(base.right, items)

            def get_result(self):
                return self.value

        init = Peoples()
        init.make_search(root, item)
        return init.get_result()

    def object_by_key(self, root, key):
        if root is not None:
            if root.data > key:
                return self.object_by_key(root.left, key)
            elif root.data == key:
                return root
            else:
                return self.object_by_key(root.right, key)

    def clear_requested(self, rt, clear_nodes):

        class Main:

            def __init__(self):
                self.changed_node = None

            def compile(self, base, node):
                if base is None:
                    return None

                self.compile(base.left, node)
                data = base.dict
                if data is not None and data["requested"] is not None and data["requested"] == node:
                    data["requested"] = None
                    self.changed_node = base
                    return
                self.compile(base.right, node)

            def getter(self):
                return self.changed_node

        init = Main()
        init.compile(rt, clear_nodes)

        return init.getter()

    def node_count(self):
        return self.round_up_count

    def remove_invalid_nodes(self, base, stat_base):
        if base is None:
            return
        self.remove_invalid_nodes(base.left, stat_base)
        data = base.dict
        if data is not None:
            active_date = data['min']
            current_date = datetime.datetime.now()
            time_delta = (active_date - current_date)
            total_seconds = time_delta.total_seconds()
            time_passed = total_seconds / 60
            if time_passed >= 5:
                data['active'] = True
                self.clear_requested(stat_base, base.data)
        self.remove_invalid_nodes(base.right, stat_base)


root = None
tree = BinaryTree()
root = tree.insert(root, 0, None)
root = tree.insert(root, 1, None)
root = tree.insert(root, 2, {
    "requested": 4,
    "active": False,
    'min': 2
})
root = tree.insert(root, 3, {
    "requested": None,
    "active": True,
    'min': 6
})
root = tree.insert(root, 4, {
    "requested": 2,
    "active": False,
    'min': 5
})

print(tree.clear_requested(root, 4).data)