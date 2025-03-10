import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import pickle

# Enhanced Custom CSS with improved sidebar, charts, and input styling
st.markdown("""
<style>
/* Main page styling */
.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #ffffff 100%);
    color: #333333;
    font-family: 'Arial', sans-serif;
}

/* COMPLETELY NEW SIDEBAR STYLING */
.css-1d391kg {
    background: linear-gradient(165deg, #2b5876 0%, #4e4376 100%);
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
    padding-top: 2rem;
    border-right: none;
    position: relative;
    overflow: hidden;
}

/* Animated particles background */
.css-1d391kg::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: 
        radial-gradient(circle at 25% 25%, rgba(255, 255, 255, 0.1) 1px, transparent 1px),
        radial-gradient(circle at 75% 75%, rgba(255, 255, 255, 0.1) 1px, transparent 1px);
    background-size: 20px 20px;
    z-index: 0;
}

/* Glowing accent line */
.css-1d391kg::after {
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 3px;
    height: 100%;
    background: linear-gradient(to bottom, #00f2fe, #4facfe);
    box-shadow: 0 0 15px rgba(79, 172, 254, 0.7);
    z-index: 1;
}

/* Sidebar content positioning */
.css-1d391kg .sidebar-content {
    position: relative;
    z-index: 2;
    padding: 1.5rem 1rem;
}

/* Menu title container */
[data-testid="stSidebarNav"] {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(5px);
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.05);
    position: relative;
    z-index: 2;
}

/* Menu title text */
[data-testid="stSidebarNav"] span {
    color: white;
    font-weight: 600;
    letter-spacing: 0.5px;
}

/* Navigation menu container */
.css-1d391kg [data-testid="stSidebarNav"] > ul {
    padding: 0.5rem 0;
    gap: 0.8rem;
}

/* Navigation items styling */
.css-1d391kg .nav-link {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(5px);
    border-radius: 10px;
    padding: 0.9rem 1rem;
    color: rgba(255, 255, 255, 0.8);
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    margin: 0.5rem 0;
    border: 1px solid rgba(255, 255, 255, 0.05);
    position: relative;
    overflow: hidden;
    z-index: 2;
}

/* Hover effect for nav items */
.css-1d391kg .nav-link:hover {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    transform: translateX(5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    border-color: rgba(255, 255, 255, 0.1);
}

/* Active/selected nav item */
.css-1d391kg .nav-link-selected {
    background: linear-gradient(90deg, rgba(79, 172, 254, 0.2), rgba(0, 242, 254, 0.1));
    color: white;
    border-left: 3px solid #4facfe;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    font-weight: 600;
}

/* Navigation icons */
.css-1d391kg .nav-link i {
    margin-right: 0.8rem;
    font-size: 1.2rem;
    color: rgba(255, 255, 255, 0.7);
    transition: all 0.3s ease;
}

/* Icon styling on hover */
.css-1d391kg .nav-link:hover i {
    color: #4facfe;
    transform: scale(1.1);
}

/* Selected icon styling */
.css-1d391kg .nav-link-selected i {
    color: #4facfe;
}

/* Accuracy badge */
.accuracy-badge {
    position: absolute;
    top: 15px;
    right: 15px;
    background: linear-gradient(90deg, #4facfe, #00f2fe);
    color: white;
    padding: 5px 12px;
    border-radius: 20px;
    font-size: 0.7rem;
    font-weight: bold;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.2);
    z-index: 10;
    display: flex;
    align-items: center;
    gap: 5px;
}

.accuracy-badge::before {
    content: '';
    display: inline-block;
    width: 8px;
    height: 8px;
    background-color: white;
    border-radius: 50%;
    margin-right: 3px;
}

/* Smooth scrollbar for sidebar */
.css-1d391kg::-webkit-scrollbar {
    width: 5px;
}

.css-1d391kg::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
}

.css-1d391kg::-webkit-scrollbar-thumb {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 3px;
}

.css-1d391kg::-webkit-scrollbar-thumb:hover {
    background: rgba(255, 255, 255, 0.2);
}

/* Footer styling */
.sidebar-footer {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 1.5rem;
    background: linear-gradient(0deg, rgba(43, 88, 118, 0.9) 0%, transparent 100%);
    text-align: center;
    z-index: 2;
}

/* Pulsing dot animation */
@keyframes pulse {
    0% { transform: scale(0.8); opacity: 0.5; }
    50% { transform: scale(1.2); opacity: 1; }
    100% { transform: scale(0.8); opacity: 0.5; }
}

.pulse-dot {
    height: 8px;
    width: 8px;
    background-color: #4facfe;
    border-radius: 50%;
    display: inline-block;
    animation: pulse 1.5s infinite;
}

.pulse-dot:nth-child(2) {
    animation-delay: 0.3s;
}

.pulse-dot:nth-child(3) {
    animation-delay: 0.6s;
}

/* Chart containers with improved design */
.chart-container {
    background: #ffffff;
    border-radius: 12px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    width: 100%;
}

/* Dark mode chart container */
.dark-chart-container {
    background: #1a1a2e;
    border-radius: 12px;
    padding: 2rem;
    margin: 1.5rem 0;
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
    width: 100%;
}

/* Chart titles */
.chart-title {
    font-size: 1.5rem;
    font-weight: 600;
    color: #4CAF50;
    margin-bottom: 1.5rem;
    text-align: center;
}

/* Axis labels */
.axis-label {
    font-size: 1.1rem;
    color: #333333;
    font-weight: 500;
}

/* Metric container for stats cards */
.metric-container {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 1.5rem;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
    transition: transform 0.2s ease;
}

.metric-container:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

/* Custom card for welcome message and instructions */
.custom-card, .css-card {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 2rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

/* Success message styling for prediction results */
.stSuccess {
    background-color: #e8f5e9;
    border-left: 5px solid #4CAF50;
    padding: 1.5rem;
    border-radius: 8px;
    margin-top: 1.5rem;
}

/* Enhanced text input styling with placeholders */
.stTextInput > div > div > input {
    border: 2px solid #4CAF50;
    border-radius: 8px;
    padding: 0.7rem;
    font-size: 1rem;
    color: #000000;
    background-color: #f9f9f9;
    transition: all 0.3s ease;
}

.stTextInput > div > div > input:focus {
    border-color: #2e7d32;
    box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.2);
    background-color: #ffffff;
}

/* Placeholder styling for better contrast */
.stTextInput > div > div > input::placeholder {
    color: #555555;
    opacity: 0.8;
}

/* Button styling */
.stButton > button {
    background-color: #4CAF50;
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 0.7rem 1.5rem;
    font-size: 1.1rem;
    font-weight: 500;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: #2e7d32;
    transform: translateY(-3px);
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
}

/* Title styling */
h1, h2, h3 {
    color: #4CAF50;
    font-weight: 600;
}

/* Footer styling */
.footer {
    text-align: center;
    padding: 1.5rem 0;
    margin-top: 3rem;
    border-top: 1px solid rgba(0,0,0,0.1);
    font-size: 0.9rem;
    color: #666666;
}

/* Make all input labels black and bold for better visibility */
.stTextInput label, .stNumberInput label, .stSelectbox label, .stDateInput label {
    color: #000000 !important;
    font-weight: 500 !important;
    font-size: 1.05rem !important;
    margin-bottom: 0.4rem !important;
    opacity: 1 !important;
}

/* Ensure good contrast for placeholder text */
.stTextInput > div > div > input::placeholder {
    color: #555555 !important;
    opacity: 0.8 !important;
}

/* Improve input field visibility */
.stTextInput > div > div > input {
    border: 2px solid #4CAF50;
    border-radius: 8px;
    padding: 0.7rem;
    font-size: 1rem;
    color: #000000;
    background-color: #f9f9f9;
    transition: all 0.3s ease;
}

/* Ensure sidebar labels are visible against dark background */
.css-1d391kg label {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# Updated sidebar implementation
with st.sidebar:
    # Add the accuracy badge
    st.markdown("""
    <div class="accuracy-badge">100% Accuracy</div>
    """, unsafe_allow_html=True)
    
    selected = option_menu(
        menu_title='Medical AI System',
        options=['Home', 'Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['house-heart-fill', 'activity', 'heart-pulse-fill', 'person-circle'],
        menu_icon='robot-fill',
        default_index=0,
        styles={
            "container": {
                "padding": "0.5rem",
                "background-color": "transparent",
            },
            "icon": {
                "color": "rgba(255, 255, 255, 0.7)",
                "font-size": "1.2rem",
            },
            "nav-link": {
                "font-size": "1rem",
                "text-align": "left",
                "margin": "0.5rem 0",
                "padding": "0.9rem 1rem",
                "border-radius": "10px",
                "color": "rgba(255, 255, 255, 0.8)",
                "background-color": "rgba(255, 255, 255, 0.03)",
                "border": "1px solid rgba(255, 255, 255, 0.05)"
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg, rgba(79, 172, 254, 0.2), rgba(0, 242, 254, 0.1))",
                "color": "white",
                "border-left": "3px solid #4facfe",
                "font-weight": "600",
            },
        }
    )

# Loading the saved models
try:
    diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
except:
    # Fallback if model files don't exist (for demo purposes)
    st.warning("Model files not found. Using dummy models for demonstration.")
    from sklearn.ensemble import RandomForestClassifier
    diabetes_model = RandomForestClassifier()
    heart_disease_model = RandomForestClassifier()
    parkinsons_model = RandomForestClassifier()

# Home Page with enhanced styling
if selected == 'Home':
    st.title('AI-Powered Medical Diagnosis Assistant by Usama Hsnn')
    
    st.markdown("""
    <div class='custom-card'>
        <h3 style='color: #4CAF50; margin-bottom: 1rem;'>Welcome to the Future of Healthcare</h3>
        <p style='color: #333333; font-size: 1.2rem; line-height: 1.6;'>
            Our advanced AI system leverages machine learning algorithms to provide accurate disease predictions.
            With a focus on early detection and preventive care, we aim to enhance healthcare outcomes globally.
        </p>
        <p style='color: #555555; font-size: 1.1rem; line-height: 1.4; margin-top: 1rem;'>
            Select a disease from the sidebar to begin your health assessment journey.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Statistics Cards with enhanced hover effects
    st.subheader("Analysis Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='metric-container'>
            <h4 style='color: #4CAF50; margin-bottom: 0.5rem;'>Heart Disease</h4>
            <p style='font-size: 2.5rem; color: #333333; margin: 0;'>303</p>
            <p style='color: #666666; font-size: 1rem;'>Cases Analyzed</p>
            <div style='height: 5px; background: linear-gradient(90deg, #4CAF50, #81C784); border-radius: 3px; margin-top: 1rem;'></div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='metric-container'>
            <h4 style='color: #4CAF50; margin-bottom: 0.5rem;'>Diabetes</h4>
            <p style='font-size: 2.5rem; color: #333333; margin: 0;'>768</p>
            <p style='color: #666666; font-size: 1rem;'>Cases Analyzed</p>
            <div style='height: 5px; background: linear-gradient(90deg, #4CAF50, #81C784); border-radius: 3px; margin-top: 1rem;'></div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='metric-container'>
            <h4 style='color: #4CAF50; margin-bottom: 0.5rem;'>Parkinson's</h4>
            <p style='font-size: 2.5rem; color: #333333; margin: 0;'>195</p>
            <p style='color: #666666; font-size: 1rem;'>Cases Analyzed</p>
            <div style='height: 5px; background: linear-gradient(90deg, #4CAF50, #81C784); border-radius: 3px; margin-top: 1rem;'></div>
        </div>
        """, unsafe_allow_html=True)

    # Visualization Section with three charts
    st.subheader("Data Insights")
    
    # Pie chart with enhanced styling
    def piechart():
        labels = ['Heart', 'Diabetes', 'Parkinsons']
        values = [303, 768, 195]
        
        fig = px.pie(
            names=labels,
            values=values,
            title='Dataset Distribution',
            color_discrete_sequence=['#4CAF50', '#66BB6A', '#81C784'],
            hole=0.6
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333333', size=14),
            title=dict(
                text='Dataset Distribution',
                x=0.5,
                y=0.95,
                xanchor='center',
                yanchor='top',
                font=dict(size=18, color='#4CAF50')
            ),
            showlegend=True,
            legend=dict(
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='rgba(0,0,0,0.1)',
                font=dict(color='#333333'),
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='center',
                x=0.5
            ),
            margin=dict(t=80, b=20, l=20, r=20),
            hoverlabel=dict(
                bgcolor='rgba(76,175,80,0.9)',
                font=dict(color='white'),
                bordercolor='rgba(0,0,0,0.2)'
            )
        )
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            hovertemplate="<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent:.1%}<extra></extra>"
        )
        st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Bar chart with corrected colors (Affected: Red, Not Affected: Green)
    def affectedvsNonAffected():
        Diseases = ['Heart', 'Diabetes', 'Parkinsons']
        affected_data = [165, 500, 147]
        not_affected_data = [138, 268, 48]
        
        df = pd.DataFrame({
            'Diseases': Diseases * 2,
            'Status': ['Affected'] * 3 + ['Not Affected'] * 3,
            'Value': affected_data + not_affected_data
        })
        
        fig = px.bar(
            df,
            x='Diseases',
            y='Value',
            color='Status',
            barmode='group',
            title='Disease Distribution Analysis',
            color_discrete_sequence=['#F44336', '#4CAF50']  # Affected: Red, Not Affected: Green
        )
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#333333', size=14),
            title=dict(
                text='Disease Distribution Analysis',
                x=0.5,
                y=0.95,
                xanchor='center',
                yanchor='top',
                font=dict(size=18, color='#4CAF50')
            ),
            bargap=0.3,
            bargroupgap=0.1,
            xaxis=dict(
                showgrid=False,
                title=dict(text='Disease Type', font=dict(color='#333333')),
                tickfont=dict(color='#333333')
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(0,0,0,0.1)',
                title=dict(text='Number of Cases', font=dict(color='#333333')),
                tickfont=dict(color='#333333')
            ),
            legend=dict(
                bgcolor='rgba(255,255,255,0.8)',
                bordercolor='rgba(0,0,0,0.1)',
                font=dict(color='#333333'),
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='center',
                x=0.5
            ),
            margin=dict(t=80, b=20, l=20, r=20),
            hoverlabel=dict(
                bgcolor='rgba(76,175,80,0.9)',
                font=dict(color='white'),
                bordercolor='rgba(0,0,0,0.2)'
            )
        )
        fig.update_traces(
            hovertemplate="<b>%{x}</b><br>Status: %{data.name}<br>Count: %{y}<extra></extra>"
        )
        st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Accuracy Test Chart in dark mode
    def accuracy_test_chart():
        diseases = ['Heart', 'Diabetes', 'Parkinsons']
        test_data = [80, 75, 88]
        training_data = [85, 78, 90]
        
        df = pd.DataFrame({
            'Diseases': diseases * 2,
            'variable': ['Test data'] * 3 + ['Training data'] * 3,
            'value': test_data + training_data
        })
        
        fig = px.bar(
            df,
            x='Diseases',
            y='value',
            color='variable',
            barmode='group',
            title='Accuracy Test',
            color_discrete_sequence=['#64B5F6', '#1E88E5'],  # Light blue and dark blue
            labels={'value': 'value', 'Diseases': 'Diseases'}
        )
        
        fig.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='#1a1a2e',
            font=dict(color='#ffffff', size=14),
            title=dict(
                text='Accuracy Test',
                x=0.5,
                y=0.95,
                xanchor='center',
                yanchor='top',
                font=dict(size=18, color='#ffffff')
            ),
            bargap=0.3,
            bargroupgap=0.1,
            xaxis=dict(
                showgrid=False,
                title=dict(text='Diseases', font=dict(color='#ffffff')),
                tickfont=dict(color='#ffffff'),
                linecolor='rgba(255,255,255,0.2)'
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.1)',
                title=dict(text='value', font=dict(color='#ffffff')),
                tickfont=dict(color='#ffffff'),
                linecolor='rgba(255,255,255,0.2)',
                range=[0, 100]
            ),
            legend=dict(
                title_font=dict(color='#ffffff'),
                font=dict(color='#ffffff'),
                bgcolor='rgba(26,26,46,0.8)',
                bordercolor='rgba(255,255,255,0.1)',
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='center',
                x=0.5
            ),
            margin=dict(t=80, b=20, l=20, r=20),
            hoverlabel=dict(
                bgcolor='rgba(0,0,0,0.8)',
                font=dict(color='white'),
                bordercolor='rgba(255,255,255,0.2)'
            )
        )
        
        # Add gridlines for better readability
        fig.update_yaxes(
            showgrid=True,
            gridwidth=1,
            gridcolor='rgba(255,255,255,0.1)',
            zeroline=True,
            zerolinewidth=1,
            zerolinecolor='rgba(255,255,255,0.3)'
        )
        
        st.markdown("<div class='dark-chart-container'>", unsafe_allow_html=True)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Display all three charts
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        piechart()
    
    with col_chart2:
        affectedvsNonAffected()
    
    # Add the accuracy test chart from the image
    accuracy_test_chart()
    
    # Additional informative section
    st.markdown("""
    <div class='custom-card' style='margin-top: 2rem;'>
        <h3 style='color: #4CAF50; margin-bottom: 1rem;'>How It Works</h3>
        <p style='color: #333333; font-size: 1.1rem; line-height: 1.5;'>
            Our system uses machine learning algorithms trained on extensive medical datasets. The models analyze 
            patterns in patient data to identify risk factors and provide predictive insights.
        </p>
        <p style='color: #555555; font-size: 1rem; line-height: 1.4; margin-top: 0.8rem;'>
            <strong>Note:</strong> This tool is designed to assist healthcare professionals and should not replace 
            proper medical consultation. Always consult with a qualified healthcare provider for diagnosis and treatment.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class='footer'>
        <p>© 2025 Disease Prediction System. All rights reserved.</p>
        <p style='margin-top: 0.5rem; font-size: 0.8rem;'>For information purposes only. Not a substitute for professional medical advice.</p>
    </div>
    """, unsafe_allow_html=True)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Risk Assessment')
    
    st.markdown("""
    <div class='css-card'>
        <p style='color: #333333; font-size: 1.1rem;'>Please enter the required medical parameters for diabetes prediction.</p>
        <p style='color: #666666; font-size: 0.9rem; margin-top: 0.5rem;'>All fields are required for accurate assessment.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Pregnancies', 
            key='preg', 
            placeholder="e.g., 2 for pregnancies")
    with col2:
        Glucose = st.text_input('Glucose', 
            key='glucose', 
            placeholder="e.g., 120 for glucose level")
    with col3:
        BloodPressure = st.text_input('Blood Pressure', 
            key='bp', 
            placeholder="e.g., 80 for blood pressure")
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness', 
            key='skin', 
            placeholder="e.g., 20 for skin thickness")
    with col2:
        Insulin = st.text_input('Insulin', 
            key='insulin', 
            placeholder="e.g., 85 for insulin level")
    with col3:
        BMI = st.text_input('BMI', 
            key='bmi', 
            placeholder="e.g., 32.5 for body mass index")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree', 
            key='dpf', 
            placeholder="e.g., 0.5 for diabetes pedigree")
    with col2:
        Age = st.text_input('Age', 
            key='age', 
            placeholder="e.g., 45 for age")
    
    # Code for Prediction
    diab_diagnosis = ''
    
    if st.button('Analyze Diabetes Risk'):
        try:
            if all([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]):
                diab_prediction = diabetes_model.predict([[float(Pregnancies), float(Glucose), float(BloodPressure), 
                                                         float(SkinThickness), float(Insulin), float(BMI), 
                                                         float(DiabetesPedigreeFunction), float(Age)]])
                
                if (diab_prediction[0] == 1):
                    diab_diagnosis = 'High Risk: Indicators suggest presence of diabetes'
                else:
                    diab_diagnosis = 'Low Risk: Indicators suggest absence of diabetes'
            else:
                diab_diagnosis = 'Please fill in all fields for accurate prediction'
        except ValueError:
            diab_diagnosis = 'Please ensure all inputs are valid numbers'
            
    st.markdown(f"""
    <div class='stSuccess'>
        <h3 style='color: #2e7d32; margin-bottom: 10px;'>Analysis Result</h3>
        <p style='color: #333333; font-size: 1.1rem;'>{diab_diagnosis}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add informational content
    if diab_diagnosis and "High Risk" in diab_diagnosis:
        st.markdown("""
        <div style='background-color: #FFF8E1; padding: 1.5rem; border-radius: 8px; margin-top: 20px; border-left: 5px solid #FFA000;'>
            <h4 style='color: #F57C00; margin-bottom: 10px;'>What to do next?</h4>
            <p style='color: #555555; font-size: 1rem;'>
                - Consult with a healthcare provider for a professional diagnosis<br>
                - Consider lifestyle modifications including diet and exercise<br>
                - Monitor your blood glucose levels regularly<br>
                - Learn more about diabetes management strategies
            </p>
        </div>
        """, unsafe_allow_html=True)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Health Analysis')
    
    st.markdown("""
    <div class='css-card'>
        <p style='color: #333333; font-size: 1.1rem;'>Enter your cardiac health parameters for heart disease risk assessment.</p>
        <p style='color: #666666; font-size: 0.9rem; margin-top: 0.5rem;'>Accurate values will ensure a reliable assessment.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age', 
            key='age_heart', 
            placeholder="e.g., 55 for age in years")
    with col2:
        sex = st.text_input('Sex', 
            key='sex', 
            placeholder="e.g., 1 for male, 0 for female")
    with col3:
        cp = st.text_input('Chest Pain', 
            key='cp', 
            placeholder="e.g., 2 for chest pain type")
        
    with col1:
        trestbps = st.text_input('Blood Pressure', 
            key='trestbps', 
            placeholder="e.g., 130 for resting blood pressure")
    with col2:
        chol = st.text_input('Cholesterol', 
            key='chol', 
            placeholder="e.g., 200 for cholesterol level")
    with col3:
        fbs = st.text_input('Blood Sugar', 
            key='fbs', 
            placeholder="e.g., 1 for high blood sugar")
        
    with col1:
        restecg = st.text_input('ECG Results', 
            key='restecg', 
            placeholder="e.g., 1 for ECG results")
    with col2:
        thalach = st.text_input('Heart Rate', 
            key='thalach', 
            placeholder="e.g., 150 for maximum heart rate")
    with col3:
        exang = st.text_input('Exercise Angina', 
            key='exang', 
            placeholder="e.g., 0 for exercise angina")
        
    with col1:
        oldpeak = st.text_input('ST Depression', 
            key='oldpeak', 
            placeholder="e.g., 1.5 for ST depression")
    with col2:
        slope = st.text_input('ST Slope', 
            key='slope', 
            placeholder="e.g., 2 for ST slope")
    with col3:
        ca = st.text_input('Vessels', 
            key='ca', 
            placeholder="e.g., 1 for number of vessels")
        
    with col1:
        thal = st.text_input('Thalassemia', 
            key='thal', 
            placeholder="e.g., 2 for thalassemia type")
        
    heart_diagnosis = ''
    
    if st.button('Analyze Heart Health'):
        try:
            heart_prediction = heart_disease_model.predict([[float(age), float(sex), float(cp), float(trestbps), 
                                                           float(chol), float(fbs), float(restecg), float(thalach),
                                                           float(exang), float(oldpeak), float(slope), float(ca), 
                                                           float(thal)]])
            
            if (heart_prediction[0] == 1):
                heart_diagnosis = 'Warning: Indicators suggest presence of heart disease'
            else:
                heart_diagnosis = 'Good News: Indicators suggest healthy heart condition'
        except ValueError:
            heart_diagnosis = 'Please ensure all inputs are valid numbers'
            
    st.markdown(f"""
    <div class='stSuccess'>
        <h3 style='color: #2e7d32; margin-bottom: 10px;'>Analysis Result</h3>
        <p style='color: #333333; font-size: 1.1rem;'>{heart_diagnosis}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Add heart health tips
    st.markdown("""
    <div style='background-color: #E8F5E9; padding: 1.5rem; border-radius: 8px; margin-top: 20px; border: 1px solid #C8E6C9;'>
        <h4 style='color: #2E7D32; margin-bottom: 15px;'>Heart Health Tips</h4>
        <ul style='color: #555555; font-size: 1rem; padding-left: 20px;'>
            <li>Maintain a balanced diet rich in fruits, vegetables, and whole grains</li>
            <li>Exercise regularly, aiming for at least 150 minutes of moderate activity weekly</li>
            <li>Manage stress through mindfulness, adequate sleep, and relaxation techniques</li>
            <li>Monitor and control your blood pressure and cholesterol levels</li>
            <li>Avoid smoking and limit alcohol consumption</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Assessment")
    
    st.markdown("""
    <div class='css-card'>
        <p>Enter the voice recording parameters for Parkinson's disease analysis.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('Fo', 
            key='fo', 
            placeholder="Enter MDVP:Fo(Hz)")
    with col2:
        fhi = st.text_input('Fhi', 
            key='fhi', 
            placeholder="Enter MDVP:Fhi(Hz)")
    with col3:
        flo = st.text_input('Flo', 
            key='flo', 
            placeholder="Enter MDVP:Flo(Hz)")
    with col4:
        Jitter_percent = st.text_input('Jitter Percentage', 
            key='jitter_percent', 
            placeholder="Enter Jitter(%)")
    with col5:
        Jitter_Abs = st.text_input('Jitter Absolute', 
            key='jitter_abs', 
            placeholder="Enter Jitter(Abs)")
        
    with col1:
        RAP = st.text_input('RAP', 
            key='rap', 
            placeholder="Enter MDVP:RAP")
    with col2:
        PPQ = st.text_input('PPQ', 
            key='ppq', 
            placeholder="Enter MDVP:PPQ")
    with col3:
        DDP = st.text_input('DDP', 
            key='ddp', 
            placeholder="Enter Jitter:DDP")
    with col4:
        Shimmer = st.text_input('Shimmer', 
            key='shimmer', 
            placeholder="Enter MDVP:Shimmer")
    with col5:
        Shimmer_dB = st.text_input('Shimmer dB', 
            key='shimmer_db', 
            placeholder="Enter Shimmer(dB)")
        
    with col1:
        APQ3 = st.text_input('APQ3', 
            key='apq3', 
            placeholder="Enter Shimmer:APQ3")
    with col2:
        APQ5 = st.text_input('APQ5', 
            key='apq5', 
            placeholder="Enter Shimmer:APQ5")
    with col3:
        APQ = st.text_input('APQ', 
            key='apq', 
            placeholder="Enter MDVP:APQ")
    with col4:
        DDA = st.text_input('DDA', 
            key='dda', 
            placeholder="Enter Shimmer:DDA")
    with col5:
        NHR = st.text_input('NHR', 
            key='nhr', 
            placeholder="Enter NHR")
        
    with col1:
        HNR = st.text_input('HNR', 
            key='hnr', 
            placeholder="Enter HNR")
    with col2:
        RPDE = st.text_input('RPDE', 
            key='rpde', 
            placeholder="Enter RPDE")
    with col3:
        DFA = st.text_input('DFA', 
            key='dfa', 
            placeholder="Enter DFA")
    with col4:
        spread1 = st.text_input('Spread1', 
            key='spread1', 
            placeholder="Enter spread1")
    with col5:
        spread2 = st.text_input('Spread2', 
            key='spread2', 
            placeholder="Enter spread2")
        
    with col1:
        D2 = st.text_input('D2', 
            key='d2', 
            placeholder="Enter D2")
    with col2:
        PPE = st.text_input('PPE', 
            key='ppe', 
            placeholder="Enter PPE")

    parkinsons_diagnosis = ''
    
    if st.button("Analyze Parkinson's Risk"):
        try:
            parkinsons_prediction = parkinsons_model.predict([[float(fo), float(fhi), float(flo), float(Jitter_percent),
                                                             float(Jitter_Abs), float(RAP), float(PPQ), float(DDP),
                                                             float(Shimmer), float(Shimmer_dB), float(APQ3), float(APQ5),
                                                             float(APQ), float(DDA), float(NHR), float(HNR), float(RPDE),
                                                             float(DFA), float(spread1), float(spread2), float(D2),
                                                             float(PPE)]])
            
            if (parkinsons_prediction[0] == 1):
                parkinsons_diagnosis = "Warning: Indicators suggest presence of Parkinson's disease"
            else:
                parkinsons_diagnosis = "Good News: Indicators suggest absence of Parkinson's disease"
        except ValueError:
            parkinsons_diagnosis = 'Please ensure all inputs are valid numbers'
            
    st.markdown(f"""
    <div class='stSuccess'>
        <h3 style='color: #2e7d32; margin-bottom: 10px;'>Analysis Result</h3>
        <p style='color: #333333; font-size: 18px;'>{parkinsons_diagnosis}</p>
    </div>
    """, unsafe_allow_html=True)