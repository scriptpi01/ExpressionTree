class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Expression_Tree:
    def __init__(self):
        self.root = None

    def is_operator(self, value):
        return value in ['+', '-', '*', '/']

    def construct_tree(self, data):
        if self.is_operator(data[0]):
            self.root = self.construct_from_prefix(data)
        elif self.is_operator(data[-1]):
            self.root = self.construct_from_postfix(data)
        else:
            print("Invalid input!")
            exit()

    def construct_from_prefix(self, data):
        i = len(data) - 3
        while len(data) > 1 and i >= 0:
            if self.is_operator(data[i]) and not self.is_operator(data[i+1]) and not self.is_operator(data[i+2]):
                # Construct the node
                node = Node(data[i])
                node.left = data[i+1] if isinstance(data[i+1], Node) else Node(data[i+1])
                node.right = data[i+2] if isinstance(data[i+2], Node) else Node(data[i+2])

                # Replace the operator and its operands with the constructed node
                data[i:i+3] = [node]

                # Reset the index to the third last element
                i = len(data) - 3
            else:
                i -= 1
        return data[0]
    
    def construct_from_postfix(self, data):
        i = 0
        while len(data) > 1:
            # If a valid operator-operand combination is found
            if i + 2 < len(data) and not self.is_operator(data[i]) and not self.is_operator(data[i+1]) and self.is_operator(data[i+2]):
                # Construct the node
                node = Node(data[i+2])
                node.left = data[i] if isinstance(data[i], Node) else Node(data[i])
                node.right = data[i+1] if isinstance(data[i+1], Node) else Node(data[i+1])

                # Replace the operands and their operator with the constructed node
                data[i:i+3] = [node]
                i = 0  # Reset the index to start
            else:
                i += 1
        return data[0]

    def print_prefix(self, node):
        if node:
            return str(node.data) + " " + self.print_prefix(node.left) + self.print_prefix(node.right)
        return ""

    def print_infix_with_parentheses(self, node):
        if node:
            if self.is_operator(node.data):
                return "(" + self.print_infix_with_parentheses(node.left) + " " + str(node.data) + " " + self.print_infix_with_parentheses(node.right) + ")"
            else:
                return str(node.data)
        return ""

    def print_infix_with_out_parentheses(self, node):
        if node:
            if self.is_operator(node.data):
                return self.print_infix_with_out_parentheses(node.left) + " " + str(node.data) + " " + self.print_infix_with_out_parentheses(node.right)
            else:
                return str(node.data)
        return ""

    def print_postfix(self, node):
        if node:
            return self.print_postfix(node.left) + self.print_postfix(node.right) + str(node.data) + " "
        return ""

def is_valid_character(item):
    """Validate if the character is a digit (0-9) or an operator."""
    return item in ['+', '-', '*', '/'] or item.isdigit()

def convert_to_number(input_list):
    for item in input_list:
        if not is_valid_character(item):
            print("Invalid character detected:", item)
            exit()
    return [int(item) if item.isdigit() else item for item in input_list]

# Expression input
input_expression = input("Input: ").split()
converted_list = convert_to_number(input_expression)

# Create tree and print expressions
tree = Expression_Tree()
tree.construct_tree(converted_list)
print("Infix (with out parentheses):", tree.print_infix_with_out_parentheses(tree.root))
print("Infix (with parentheses):", tree.print_infix_with_parentheses(tree.root))
print("Prefix:", tree.print_prefix(tree.root).strip())
print("Postfix:", tree.print_postfix(tree.root).strip())
