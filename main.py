import streamlit as st


def main():
    st.title("Hi ShaHar, Testing streamlit")

    # Get user input
    field1 = st.text_input("Field 1")
    field2 = st.text_input("Field 2")
    field3 = st.text_input("Field 3")
    if st.button("print fields"):
        st.write(field1, field2, field3)


if __name__ == "__main__":
    main()
