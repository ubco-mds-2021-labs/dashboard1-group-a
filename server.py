from src.app import app, server
from src.layout import LAYOUT

# Import Callbacks
from src.components.example_dropdown import update_example_slider_from_example_dropdown

app.layout = LAYOUT

if __name__ == "__main__":
    app.run_server(debug=True)
