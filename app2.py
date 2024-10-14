import streamlit as st
import math

def scientific_calculator(num1, num2, operation, angle=None):
    if operation == 'Addition':
        return num1 + num2
    elif operation == 'Subtraction':
        return num1 - num2
    elif operation == 'Multiplication':
        return num1 * num2
    elif operation == 'Division':
        return num1 / num2 if num2 != 0 else "Error! Division by zero."
    elif operation == 'Exponentiation':
        return math.pow(num1, num2)
    elif operation == 'Logarithm (base 10)':
        return math.log10(num1)
    elif operation in ['Sine', 'Cosine', 'Tangent']:
        radian = math.radians(angle)
        if operation == 'Sine':
            return math.sin(radian)
        elif operation == 'Cosine':
            return math.cos(radian)
        elif operation == 'Tangent':
            return math.tan(radian)

# Streamlit app
st.title("Scientific Calculator")

# User inputs
operation = st.selectbox("Select operation:", 
                          ("Addition", "Subtraction", "Multiplication", "Division", 
                           "Exponentiation", "Logarithm (base 10)", "Sine", 
                           "Cosine", "Tangent"))

num1 = st.number_input("Enter first number:", value=0.0)
num2 = None
angle = None

if operation in ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Logarithm (base 10)']:
    num2 = st.number_input("Enter second number:", value=0.0)
if operation in ['Sine', 'Cosine', 'Tangent']:
    angle = st.number_input("Enter angle in degrees:", value=0.0)

if st.button("Calculate"):
    if operation in ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Logarithm (base 10)']:
        result = scientific_calculator(num1, num2, operation)
    else:
        result = scientific_calculator(num1, num2, operation, angle)
    
    st.write(f"The result is: {result}")

