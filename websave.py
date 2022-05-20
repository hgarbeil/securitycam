import dash
import dash_html_components as html
from dash.dependencies import Input,Output
import glob
import os
import time

def get_file_list ():
	# get jpeg files
	list0 = filter(os.path.isfile,glob.glob("assets/*.jpg"))
	jpegs = sorted(list0, key=os.path.getctime)
	jpegs.reverse()
	# get mp4 files
	list1 = filter(os.path.isfile,glob.glob("assets/*.mp4"))
	mp4s = sorted(list1, key=os.path.getmtime)
	mp4s.reverse()
	return (jpegs,mp4s)
	


jpegs,mp4s=get_file_list()
print("jpeg : ", jpegs[0])
print("mp4 : ", mp4s[0])

app = dash.Dash(__name__)

app.layout = html.Div(children = [
	html.Pre("Selected Video"),
	html.Div([
	dash.dcc.Dropdown(
		id="mpeg-dd",
		options= mp4s,
		value=mp4s[0],
		)],style={'width':'40%'}),
	html.Pre("------------------"),
	html.Div(id='vid_placeholder'),
	html.Pre("Selected JPEG"),
	html.Div([
	dash.dcc.Dropdown(
		id="jpeg-dd",
		options= jpegs,
		value=jpegs[0],
		)
	],style={'width':'40%'}),
	html.Pre("------------------"),
	#dash.dcc.Graph(id='my_jpeg'),
	html.Div(id='img_placeholder'),
    ])



@app.callback(
	[Output('vid_placeholder', 'children')],
	[Output('img_placeholder', 'children')],
	[Input('mpeg-dd', component_property='value')],
	[Input('jpeg-dd', component_property='value')]

)

def hello_there(val_vid,val_jpg):
        myvid = html.Video(
            controls = True,
            id = 'movie_player',
            #src = "assets/110-20220518122423.mp4",
            #src = "assets/last.mp4",
	    src = val_vid,
            autoPlay=True
        )

        imagecomp=html.Img(src=val_jpg)

        return [myvid, imagecomp]

if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
