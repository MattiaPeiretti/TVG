import flask

from project.settingsHandler import SettingsHandler

settings_handler = SettingsHandler()

def render_settings():
    if flask.request.method == "POST":
        new_settings_data = flask.request.form
        for key, value in new_settings_data.items():
            settings_handler.set_setting(key, value)
    
    settings_template = settings_handler.get_settings_template()
    settings_data = settings_handler.get_settings_data()
    
    return flask.render_template("settings.html", settings_template=settings_template, settings_data=settings_data)

def reload_settings():
    settings_handler.reload_settings_template()
    return flask.redirect("/settings")