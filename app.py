import gradio as gr

## gr.themes.Default().dump(filename="theme.json") # dump the base theme to JSON

# css = """
# #component-2-button.selected { background-color: #CC8800 }
# #component-8-button.selected { background-color: #CC8800 }
# """

css = """
#t1-button.selected { background-color: #CC8800 }
#t2-button.selected { background-color: #CC8800 }
"""

new_theme = gr.themes.Default(
    radius_size=gr.themes.sizes.radius_none, # seems to have effect
    primary_hue="blue", # does not seem to have any effect
).set(
    background_fill_primary="lightgray", # have effect when browser in LIGHT mode
    background_fill_primary_dark="darkgreen", # have effect when browser in DARK mode
)


with gr.Blocks(css=css, theme=new_theme) as demo:
    gr.Markdown("Flip text or image files using this demo.")
    with gr.Tab("Flip Text 1", elem_id="t1"):
        gr.Label("aaa")
        gr.Label("bbb")
        gr.Textbox()
        gr.Button("Button One")
    with gr.Tab("Flip Image", elem_id="t2"):
        gr.Label("cc")
        gr.Label("dd")
        gr.Label("ee")
        gr.Button("Button 2")

demo.launch()