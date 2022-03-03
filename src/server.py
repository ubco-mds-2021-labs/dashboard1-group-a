from app import app
from layout import LAYOUT

# Import Callbacks to update app dynamically
from components.example_dropdown import update_example_slider_from_example_dropdown

# For gunicorn deployment eventually.
server = app.server

app.layout = LAYOUT

if __name__ == "__main__":
    app.run_server(debug=True)
