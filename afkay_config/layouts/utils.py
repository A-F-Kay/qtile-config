from libqtile import hook, qtile


@hook.subscribe.layout_change
def on_layout_change(layt, _group):
    try:
        bar = qtile.current_screen.top
    except AttributeError:
        return

    if layt.name == "max":
        bar.show(False)
    else:
        bar.show(True)

    bar.current_screen.group.layout_all()
