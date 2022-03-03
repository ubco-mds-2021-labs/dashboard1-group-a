from src.app import app
from src.layout import LAYOUT

# Import Callbacks to update app dynamically
from src.components.example_dropdown import update_example_slider_from_example_dropdown

# For gunicorn deployment eventually.
server = app.server

app.layout = LAYOUT

if __name__ == "__main__":
    app.run_server(debug=True)
