import dash
from dash import dcc, html
import base64

boat_photo=base64.b64encode(open('resources/Titanic-2.jpg', 'rb').read())


tab_1_layout = html.Div([
    html.H3('Introduction - too cool to mess up this tab'),
    html.Div([
    html.Div([
        dcc.Markdown("This dashboard is a template for capstone presentations of machine learning. Though simple, it has several important features that should be imitated in any capstone:"),
        dcc.Markdown("* A cleaned dataset with a clearly defined problem and target variable."),
        dcc.Markdown("* A predictive model that has been trained on a portion of the data, and tested on a set-aside portion."),
        dcc.Markdown("* Evaluation metrics showing the performance of the model on the testing data."),
        dcc.Markdown("* Individual results of the testing dataset, for further analysis of incorrect predictions."),
        dcc.Markdown("* A feature to receive new user inputs that makes predictions based on the new data."),
        dcc.Markdown("* An interactive user interface deployed on a cloud platform and accessible to potential reviewers."),
<<<<<<< HEAD
        html.A('View code on github', href='https://github.com/pgelvin/505-titanic-survival-classifier.git'),
=======
        html.A('View code on github', href='https://github.com/pgelvin/505-titanic-survival-classifier.git'), 
               # href='https://github.com/plotly-dash-apps/505-titanic-survival-classifier'),
>>>>>>> e05e6a29adcf86d671928ba82f6759e8b0d626af
    ],className='ten columns'),
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(boat_photo.decode()), style={'height':'400px'}),
    ],className='two columns'),


    ],className='nine columns'),

])
