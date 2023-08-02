import streamlit as st
import plotly.express as px

def card_layout():
    # Set custom CSS for the blue background color
    st.markdown("""
    <style>
    .blue-card {
        background-color: #007BFF;
        color: white;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Create a 3-column layout
    col1, col2, col3 = st.columns(3)

    # Card 1
    with col1:
        with st.container():
            st.markdown("### Heart", unsafe_allow_html=True)
            st.write("Total Data: 303")

    # Card 2
    with col2:
        with st.container():
            st.markdown("### Diabetes", unsafe_allow_html=True)
            st.write("Total Data: 768")

    # Card 3
    with col3:
        with st.container():
            st.markdown("### Parkinsons", unsafe_allow_html=True)
            st.write("Total Data: 195")

if __name__ == '__main__':
    card_layout()

def affectedvsNonAffected():
    # Sample data for the bar graph
    Diseases = ['Heart', 'Diabetes', 'Parkinsons']
    affected_data = [165, 500, 147]  # Replace this with your actual data for the "Affected" group
    not_affected_data = [138, 268, 48]  # Replace this with your actual data for the "Not Affected" group

    # Combine data for "Affected" and "Not Affected" into a single DataFrame
    import pandas as pd
    df = pd.DataFrame({
        'Diseases': Diseases * 2,
        'Status': ['Affected'] * 3 + ['Not Affected'] * 3,
        'Value': affected_data + not_affected_data
    })

    # Create the bar graph using Plotly Express
    fig = px.bar(df, x='Diseases', y='Value', color='Status', barmode='group',
                 title='Affected vs. Not Affected Bar Graph')

    # Show the graph using Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
    affectedvsNonAffected()

def grouped_bar_graph():
    # Sample data for the grouped bar graph
    categories = ['Heart', 'Diabetes', 'Parkinsons']
    test = [0.819672131147541*100, 0.7727272727272727*100, 0.8717948717948718*100]
    training = [0.8512396694214877*100, 0.7833876221498371*100, 0.8717948717948718*100]

    # Create a DataFrame for the data
    import pandas as pd
    df = pd.DataFrame({'Diseases': categories, 'Test data': test, 'Training data': training})

    # Create the grouped bar graph using Plotly Express
    fig = px.bar(df, x='Diseases', y=['Test data', 'Training data'], barmode='group', title='Accuracy test')

    # Show the graph using Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
    grouped_bar_graph()









