import streamlit as st
import plotly.express as px

def affectedvsNonAffected():
    # Sample data for the bar graph
    Diseases = ['Heart', 'Diabetes', 'Parkinsons']
    affected_data = [165, 500, 147]  # Replace this with your actual data for the "Affected" group
    not_affected_data = [138, 268, 48]  # Replace this with your actual data for the "Not Affected" group

    # Combine data for "Affected" and "Not Affected" into a single DataFrame
    import pandas as pd
    df_affected = pd.DataFrame({
        'Diseases': Diseases,
        'Status': 'Affected',
        'Value': affected_data
    })

    df_not_affected = pd.DataFrame({
        'Diseases': Diseases,
        'Status': 'Not Affected',
        'Value': not_affected_data
    })

    df_combined = pd.concat([df_affected, df_not_affected], axis=0)

    # Create the bar graph using Plotly Express
    fig = px.bar(df_combined, x='Diseases', y='Value', color='Status', barmode='group',
                 title='Affected vs. Not Affected Bar Graph')

    # Show the graph using Streamlit
    st.plotly_chart(fig)

def grouped_bar_graph():
    # Sample data for the grouped bar graph
    categories = ['Heart', 'Diabetes', 'Parkinsons']
    test = [0.819672131147541 * 100, 0.7727272727272727 * 100, 0.8717948717948718 * 100]
    training = [0.8512396694214877 * 100, 0.7833876221498371 * 100, 0.8717948717948718 * 100]

    # Create a DataFrame for the data
    import pandas as pd
    df = pd.DataFrame({
        'Diseases': categories,
        'Test data': test,
        'Training data': training
    })

    # Create the grouped bar graph using Plotly Express
    fig = px.bar(df, x='Diseases', y=['Test data', 'Training data'], barmode='group', title='Accuracy test')

    # Show the graph using Streamlit
    st.plotly_chart(fig)

if __name__ == '__main__':
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

    # Create a single row layout
    row1 = st.columns(3)

    # Card 1
    with row1[0]:
        with st.container():
            st.markdown("### Heart", unsafe_allow_html=True)
            st.write("Total Data: 303")

        # Show the affected vs. non-affected bar graph in the first column
        affectedvsNonAffected()

    # Card 2
    with row1[1]:
        with st.container():
            st.markdown("### Diabetes", unsafe_allow_html=True)
            st.write("Total Data: 768")
    
    with row1[2]:
        with st.container():
            st.markdown("### Parkinsons", unsafe_allow_html=True)
            st.write("Total Data: 195")

        # Show the grouped bar graph in the second column
        grouped_bar_graph()
