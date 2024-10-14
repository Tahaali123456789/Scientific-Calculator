import streamlit as st
import math

# Function to perform calculations
def calculate(num1, num2, operation, angle=None):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        return num2 != 0 and (num1 / num2) or "Error! Division by zero."
    elif operation == 'Exponentiation':
        return math.pow(num1, num2)
    elif operation == 'Logarithm (base 10)':
        return num1 > 0 and math.log10(num1) or "Error! Logarithm of non-positive number."
    elif operation in ['Sine', 'Cosine', 'Tangent']:
        radian = math.radians(angle)
        if operation == 'Sine':
            return math.sin(radian)
        elif operation == 'Cosine':
            return math.cos(radian)
        elif operation == 'Tangent':
            return math.tan(radian)

# Set page configuration
st.set_page_config(page_title="Scientific Calculator", layout="wide")

# Create a black background and light grey sidebar
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #444444;  /* Dark grey for sidebar */
        color: white;
    }
    .stButton > button {
        background-color: #d3d3d3; /* Light grey for buttons */
        color: black;
    }
    </style>
    """, unsafe_allow_html=True
)

st.sidebar.header("Input Parameters")
operation = st.sidebar.selectbox("Select operation:", 
                                  ("Addition", "Subtraction", "Multiplication", 
                                   "Division", "Exponentiation", 
                                   "Logarithm (base 10)", "Sine", 
                                   "Cosine", "Tangent"))

num1 = st.sidebar.number_input("Enter first number:", value=0.0)

if operation in ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Logarithm (base 10)']:
    num2 = st.sidebar.number_input("Enter second number:", value=0.0)
else:
    num2 = None

if operation in ['Sine', 'Cosine', 'Tangent']:
    angle = st.sidebar.number_input("Enter angle in degrees:", value=0.0)
else:
    angle = None

# Calculate button
if st.sidebar.button("Calculate", key='calc_btn'):
    if operation in ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Logarithm (base 10)']:
        result = calculate(num1, num2, operation)
    else:
        result = calculate(num1, None, operation, angle)
    
    st.write(f"The result of {operation.lower()} is: {result}")

# About section
st.sidebar.header("About")
st.sidebar.info("This is a graphical scientific calculator built with Streamlit. "
                "You can perform various scientific operations including trigonometry, "
                "exponentiation, and logarithms.")
