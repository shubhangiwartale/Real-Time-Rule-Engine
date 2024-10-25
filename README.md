Here's a detailed README file content that describes the project, including steps to create a repository, usage instructions, and more:

---

# Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

## Overview

This project implements a rule engine using an Abstract Syntax Tree (AST) to evaluate complex rules against user data for weather monitoring. The engine allows for the combination of multiple rules, modification of existing rules, and evaluation based on specific user attributes.

## Features

- Create AST from rule strings.
- Combine multiple ASTs into a single AST.
- Evaluate rules against user data.
- Modify existing rules dynamically.

## Requirements

- Python 3.x
- Libraries: `re` (standard library)

## Directory Structure

```
/Real-Time-Weather-Data-Processing-System
├── main.py
├── requirements.txt
└── README.md
```

## Getting Started

### Step 1: Clone the Repository

1. Open your terminal (Command Prompt, PowerShell, or Git Bash).
2. Clone the repository using the following command:

   ```bash
   git clone https://github.com/shubhangiwartale/Real-Time-Weather-Data-Processing-System.git
   ```

3. Navigate to the cloned directory:

   ```bash
   cd Real-Time-Weather-Data-Processing-System
   ```

### Step 2: Set Up Your Environment

1. **Install Required Libraries** (if any). Create a `requirements.txt` file listing all dependencies:

   ```plaintext
   # requirements.txt
   # No additional packages required for this example
   ```

2. (Optional) Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Running the Application

1. Open `main.py` in your favorite code editor.
2. You can test the rule engine using the example usage provided in the code. 

   ```python
   # Example Usage for Rule Engine with AST
   rule1 = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
   user_data = {
       'age': 35,
       'department': 'Sales',
       'salary': 60000,
       'experience': 3
   }
   print("User eligible based on combined rule:", evaluate_rule(combined_ast, user_data))
   ```

3. Run the application:

   ```bash
   python main.py
   ```

### Step 4: Modifying Rules

To modify existing rules, use the `modify_rule` function in the code. For example:

```python
modify_rule(combined_ast, "age > 30", "age > 40")
```

### Step 5: Committing Changes

1. After making changes to the code, stage and commit your changes:

   ```bash
   git add .
   git commit -m "Updated rule evaluation logic"
   ```

2. Push your changes to the remote repository:

   ```bash
   git push origin main
   ```

## MongoDB Schema Design for Rules

### Example Schema

To store the AST structure in MongoDB, consider the following schema:

```json
{
    "rule_id": "rule1",
    "root": {
        "type": "operator",
        "value": "AND",
        "left": {
            "type": "operand",
            "value": "age > 30"
        },
        "right": {
            "type": "operator",
            "value": "OR",
            "left": {
                "type": "operand",
                "value": "salary > 50000"
            },
            "right": {
                "type": "operand",
                "value": "experience > 5"
            }
        }
    }
}
```

## Non-Functional Requirements

- **Security**: Ensure user data is validated and sanitized.
- **Performance**: Optimize rule evaluation for scalability.
- **Logging**: Implement logging for rule evaluation and modifications for auditing purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please contact shubhangiwartale@gmail.com.
