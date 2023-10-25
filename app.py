import gradio as gr

# new_theme = gr.themes.Default().set(
#     radius_size=gr.themes.sizes.radius_none
# )

new_theme = gr.themes.Default(
    radius_size=gr.themes.sizes.radius_none, # seems to have effect
    primary_hue="blue" # does not seem to have any effect
).set(
    background_fill_primary = "pink", # have effect when browser in LIGHT mode
    # background_fill_primary_dark # when browser is in DARK mode
)

# gr.themes.Default().dump(filename="theme.json")

with gr.Blocks(theme=new_theme) as demo:
    gr.Markdown("Flip text or image files using this demo.")
    with gr.Tab("Flip Text 1"):
        gr.Label("aaa")
        gr.Label("bbb")
        gr.Button("Button One")
    with gr.Tab("Flip Image"):
        gr.Label("cc")
        gr.Label("dd")
        gr.Label("ee")
        gr.Button("Button 2")

demo.launch()