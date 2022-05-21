import dash
# import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash import html
from fileops import *



jpegs, mp4s = get_file_list()
print("jpeg : ", jpegs[0])
print("mp4 : ", mp4s[0])

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    dash.dcc.Interval(id='update_int', interval=30 * 1000, n_intervals=0),
    html.Div([
        html.H4 ("Maximum File Age (days)"),
    	dash.dcc.Input(id='maxdays_input',type="number", value=30),
	html.Button("Update",id='submit_button',n_clicks=0),
	], style={'width':'80%'}),
    
    html.Div([
                
		#html.Pre("Selected Video",style={'font-size':'12px'}),
		html.H3("Selected Video"),
        	dash.dcc.Dropdown(
            	id="mpeg-dd",
            	options=mp4s,
            	value=mp4s[0]),
    		html.Pre("------------------"),
    		html.Div(id='vid_placeholder'),
    ], style={'width': '48%','display':'inline-block'}),
    html.Div([
	html.H3("Selected JPG"), 
       	dash.dcc.Dropdown(
           	id="jpeg-dd",
            	options=jpegs,
                value=jpegs[0],
        	),
    	html.Pre("------------------"),
    	html.Div(id='img_placeholder'),
    ], style={'width': '48%','display':'inline-block'}),
    # dash.dcc.Graph(id='my_jpeg'),
])


@app.callback(

    [Output('vid_placeholder', 'children')],
    [Output('img_placeholder', 'children')],
    [Input('mpeg-dd', component_property='value')],
    [Input('jpeg-dd', component_property='value')]

)
def hello_there(val_vid, val_jpg):
    myvid = html.Video(
        controls=True,
        id='movie_player',
        # src = "assets/110-20220518122423.mp4",
        # src = "assets/last.mp4",
        src=val_vid,
        autoPlay=True
    	,style={'width':'98%'})
    imagecomp = html.Img(src=val_jpg, style={'width':'98%'})
    return ([myvid, imagecomp])


@app.callback(
    [Output('mpeg-dd', component_property='options')],
    [Output('jpeg-dd', component_property='options')],
    [State('maxdays_input', 'value')],
    #[Input('update_int', 'n_intervals')],
    [Input('submit_button', 'n_clicks')],
)

def update_dd(ndays,nclicks):
    jp0, mp0 = get_file_age(ndays)
    return ([mp0, jp0])


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
