import streamlit as st

st.set_page_config(page_title="Body Mass Index", page_icon="⚖️")

# Inside the page
st.title("Body Mass Index Calculator")
st.markdown("""This is a simple calculator to determine your Body Mass
             Index (BMI). Enter your height and weight below to 
            calculate your BMI.""")
st.divider()

st.subheader("Input Your Details")
weight = st.number_input("Enter you Weight (kg)",
                         min_value=0.0, value=70.0, step=0.1)

col1, col2 = st.columns(2)
with col1:
    feet = st.number_input("Enter your Height (feet)",
                           min_value=0.0, value=5.0, step=1.0)
with col2:
    inches = st.number_input("Enter your Height (inches)",
                             min_value=0.0, value=11.0, step=0.1)

st.divider()

st.subheader("Your BMI Result")
# Convert height to meters
height_m = (feet * 0.3048) + (inches * 0.0254)
bmi = weight / (height_m ** 2) if height_m > 0 else 0

# Underweight: BMI less than 18.5
# Normal (healthy weight): BMI 18.5 – 24.9
# Overweight: BMI 25.0 – 29.9
# Obesity (Class I): BMI 30.0 – 34.9
# Obesity (Class II): BMI 35.0 – 39.9
# Obesity (Class III / severe obesity): BMI 40.0 and above

if bmi < 18.5:
    st.warning(f"Your BMI is {bmi:.1f}. You are underweight.")
elif 18.5 <= bmi < 25:
    st.success(f"Your BMI is {bmi:.1f}. You have a normal weight.")
elif 25 <= bmi < 30:
    st.warning(f"Your BMI is {bmi:.1f}. You are overweight.")
else:
    if 30 <= bmi < 35:
        obesity_class = "Class I"
    elif 35 <= bmi < 40:
        obesity_class = "Class II"
    else:
        obesity_class = "Class III (severe obesity)"
    st.error(
        f"Your BMI is {bmi:.1f}. You are in the obesity category: {obesity_class}.")
