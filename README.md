# ExpressionTree

ExpressionTree is a Python implementation designed to construct and evaluate expression trees from prefix and postfix expressions. This tool is unique in its approach as it does not rely on the traditional stack-based algorithms for tree construction. Instead, it uses an innovative method that builds the expression tree directly from the given expression string.

## Features

- **Supports Prefix and Postfix Expressions**: Capable of constructing expression trees from both prefix and postfix notations.
- **Direct Tree Construction**: Builds the expression tree without using a stack, offering an alternative approach to traditional methods.
- **Infix Expression Output**: Converts the expression tree back into infix notation, both with and without parentheses.
- **Prefix and Postfix Output**: Generates the prefix and postfix notation from the constructed expression tree.
- **Operator and Operand Validation**: Ensures that the input consists of valid operators and operands.

## How It Works

The ExpressionTree class is the core of this tool. It contains methods to construct the tree and print expressions in various formats. The process involves the following steps:

1. **Tree Construction**: 
   - For prefix expressions, the tree is built by scanning the expression from right to left.
   - For postfix expressions, the tree is constructed by scanning the expression from left to right.

2. **Expression Printing**: 
   - The `print_infix_with_parentheses` and `print_infix_with_out_parentheses` methods convert the tree into infix notation.
   - The `print_prefix` method outputs the expression in prefix notation.
   - The `print_postfix` method generates the expression in postfix notation.

## Requirements

- Python 3.x

## Usage

1. **Input the Expression**:
   - Run the script.
   - Enter the expression in either prefix or postfix format when prompted.

2. **View the Results**:
   - The program will display the expression in infix (with and without parentheses), prefix, and postfix notations.

3. **Validation**:
   - The program checks for valid characters and converts numerical characters to integers.

## Example

```
Input: * + 2 3 4
Infix (without parentheses): 2 + 3 * 4
Infix (with parentheses): (2 + 3) * 4
Prefix: * + 2 3 4
Postfix: 2 3 + 4 *
```

## Contributing

Contributions to enhance the functionality or efficiency of ExpressionTree are welcome. Please feel free to fork the repository, make changes, and submit a pull request.

## Conclusion

ExpressionTree offers a novel way to construct and evaluate expression trees, especially beneficial for those looking to explore alternatives to stack-based parsing algorithms. Its ability to handle both prefix and postfix expressions and convert them into various formats makes it a versatile tool for studying and understanding expression parsing and tree construction.
