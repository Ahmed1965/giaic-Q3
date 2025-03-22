import streamlit as st


add = st.text_input("Enter Task..")

if st.button('Add'):
    if add:
        with open(r'database\task.txt','a') as f:
            f.write(add + '\n')
            st.success('Task add successfully')
    else:
        st.error('write something')
