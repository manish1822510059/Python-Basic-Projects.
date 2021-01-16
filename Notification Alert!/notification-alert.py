from pyler import notification

title = "Hello Amazing People"

message = "Drink 500ml Water"

notification.notify(title=title, meaage=message,
                    app_icon=None, timeout=10, toast=False)
