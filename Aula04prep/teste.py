import gradio as gr

def hello(name):
    return f"Olá, {name}!"

iface = gr.Interface(fn=hello, inputs="text", outputs="text")
iface.launch()
