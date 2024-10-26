# Node class to represent an AST node
class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"


# Function to create an AST from a rule string
import re

def create_rule(rule_string):
    tokens = re.findall(r'\(|\)|\w+|[><=]+|AND|OR', rule_string)

    def parse(tokens):
        stack = []
        for token in tokens:
            if token in ('AND', 'OR'):
                right = stack.pop()
                left = stack.pop()
                stack.append(Node('operator', value=token, left=left, right=right))
            elif token not in ('(', ')'):
                stack.append(Node('operand', value=token))
        return stack[0]
    
    return parse(tokens)


# Function to combine multiple ASTs into one AST
def combine_rules(rule_asts):
    if len(rule_asts) == 1:
        return rule_asts[0]
    
    combined_rule = rule_asts[0]
    for rule in rule_asts[1:]:
        combined_rule = Node('operator', value='AND', left=combined_rule, right=rule)
    
    return combined_rule


# Function to evaluate an AST against user data
def evaluate_rule(ast, user_data):
    if ast.type == 'operand':
        components = ast.value.split()
        if len(components) == 3:
            key, operator, value = components
            value = value.strip("'")
        elif len(components) == 1:
            key = components[0]
            return user_data.get(key, False)
        else:
            raise ValueError(f"Unexpected operand format: {ast.value}")

        if key not in user_data:
            return False

        if operator == '>':
            return user_data[key] > int(value)
        elif operator == '<':
            return user_data[key] < int(value)
        elif operator == '=':
            return user_data[key] == value
    elif ast.type == 'operator':
        left_eval = evaluate_rule(ast.left, user_data)
        right_eval = evaluate_rule(ast.right, user_data)
        return left_eval and right_eval if ast.value == 'AND' else left_eval or right_eval


# Step 1: Create Individual Rules and Verify Their AST Representation
rules = [
    "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing'))",
    "((age > 30 AND department = 'Marketing'))"
]

rule_asts = [create_rule(rule) for rule in rules]

# Step 2: Combine the Example Rules
combined_ast = combine_rules(rule_asts)

# Step 3: Sample JSON Data and Evaluate Rule
user_data_samples = [
    {'age': 35, 'department': 'Sales'},   # Should be eligible
    {'age': 22, 'department': 'Marketing'},  # Should be eligible
    {'age': 40, 'department': 'Marketing'},  # Should be eligible
    {'age': 29, 'department': 'Finance'},    # Should not be eligible
]

results = {index + 1: evaluate_rule(combined_ast, user_data) for index, user_data in enumerate(user_data_samples)}

# Output the results in a sorted manner
for user_id, eligible in sorted(results.items()):
    print(f"User {user_id} eligible based on combined rule: {eligible}")
