import streamlit as st

# Main Streamlit app logic
def main():
    # Check the checkbox value
    checkbox_value = st.checkbox("Checkbox")

    # Perform actions based on checkbox value
    if checkbox_value:
        st.write("Checkbox is checked")
    else:
        st.write("Checkbox is unchecked")

    # Display the checkbox in the middle of the page
    st.write("This is the middle of the page")
    st.write("The checkbox will be displayed here:")
    st.checkbox("Checkbox")

# Run the main function
main()
