from dash.testing.application_runners import import_app
from dash.testing.composite import DashComposite


def test_dbap001_run_server(dash_duo):
    # Start dash app with the "app" variable from server.py
    app = import_app("server")
    dash_duo.start_server(app)

    # Ensure that the dash app runs by waiting until the "_dash-app-content"
    # section loads (the html element with our app content), or 30 seconds.
    dash_duo.wait_for_element_by_id("_dash-app-content", timeout=30)

    # Ensure no errors occured in the browser.
    assert dash_duo.get_logs() == [], "Browser console should contain no error"
