import streamlit as st 
import numpy as np
import pandas as pd
import pickle

breast_cancer_detector_model=pickle.load(open('breast_cancer_detection.pickle','rb'))


def welcome():
    return "Welcome all to the Breast Cancer Detection"

def predict(radius,
    texture,
    perimeter,
    area,
    smootness,
    compactness,
    concavity,
    concave_points,
    symmetry,
    fractal_dimension,
    radius_error,
    texture_error,
    perimeter_error,
    area_error,
    smoothness_error,
    compactness_error,
    concavity_error,
    concave_points_error,
    symmetry_error,
    fractal_dimension_error,

    worst_radius,
    worst_texture,
    worst_perimeter,
    worst_area,

    worst_smoothness,
    worst_compactness,
    worst_concavity,
    worst_concave_points,
    worst_symmetry,
    worst_fractal_dimension):

    prediction=breast_cancer_detector_model.predict([[radius,
    texture,
    perimeter,
    area,
    smootness,
    compactness,
    concavity,
    concave_points,
    symmetry,
    fractal_dimension,
    radius_error,
    texture_error,
    perimeter_error,
    area_error,
    smoothness_error,
    compactness_error,
    concavity_error,
    concave_points_error,
    symmetry_error,
    fractal_dimension_error,

    worst_radius,
    worst_texture,
    worst_perimeter,
    worst_area,

    worst_smoothness,
    worst_compactness,
    worst_concavity,
    worst_concave_points,
    worst_symmetry,
    worst_fractal_dimension]])

    print(prediction)

    if prediction == 0:
        result_var=" suffering from breast Cancer (Malignant) "
        return result_var
    elif prediction == 1:
        result_var=" not suffering from breast cancer i.e (Benign) "
        return result_var




def main():
    st.title("Breast Cancer Detection App")
    html_temp="""
    <div style="background-color:Magneta;padding:10px">
    <h2 style="color:white;text-align:center;"> Streamlit Breast Cancer Detection ML App</h2>
    </div>
    
    """

    st.markdown(html_temp,unsafe_allow_html=True)

    radius=st.text_input("Mean Radius")
    texture=st.text_input("Mean Texture")
    perimeter=st.text_input("Mean Perimeter")
    area=st.text_input("Mean Area")
    smootness=st.text_input("Mean Smootness")
    compactness=st.text_input("Mean Compactness")
    concavity=st.text_input("Mean Concave Points")
    concave_points=st.text_input("mean concave points")
    symmetry=st.text_input("Mean Symmetry")
    fractal_dimension=st.text_input("Mean Fractal Dimension")
    radius_error=st.text_input("Radius Error")
    texture_error=st.text_input("Texture error")
    perimeter_error=st.text_input("Perimeter error")
    area_error=st.text_input("area error")
    smoothness_error=st.text_input("smoothness error")
    compactness_error=st.text_input("compactness error")
    concavity_error=st.text_input("concavity error")
    concave_points_error=st.text_input("concave points error")
    symmetry_error=st.text_input("symmetry error")
    fractal_dimension_error=st.text_input("fractal dimension error")

    worst_radius=st.text_input("worst radius")
    worst_texture=st.text_input("worst texture")
    worst_perimeter=st.text_input("worst perimeter")
    worst_area=st.text_input("worst area")

    worst_smoothness=st.text_input("worst smoothness")
    worst_compactness=st.text_input("worst compactness")
    worst_concavity=st.text_input("worst concavity")
    worst_concave_points=st.text_input("worst concave points")
    worst_symmetry=st.text_input("worst symmetry")
    worst_fractal_dimension=st.text_input("worst fractal dimension")
    
    result=""
    if st.button("Predict"):
        result=predict(radius,texture,
    perimeter,
    area,
    smootness,
    compactness,
    concavity,
    concave_points,
    symmetry,
    fractal_dimension,
    radius_error,
    texture_error,
    perimeter_error,
    area_error,
    smoothness_error,
    compactness_error,
    concavity_error,
    concave_points_error,
    symmetry_error,
    fractal_dimension_error,

    worst_radius,
    worst_texture,
    worst_perimeter,
    worst_area,

    worst_smoothness,
    worst_compactness,
    worst_concavity,
    worst_concave_points,
    worst_symmetry,
    worst_fractal_dimension)

    st.success("Person is {}".format(result))
    
    st.write("Click This [ To book doctor appointment online](https://www.practo.com/doctors)")


if __name__ == '__main__':
    main()

