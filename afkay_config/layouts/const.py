from libqtile import layout


layout_cfg = {
    'margin': 3,
    'margin_on_single': 15,
    'border_focus': '#F-1D9FF',
    'border_normal': '#49453c',
    'border_width': 1,
    'border_on_single': True,
}

layouts = [
    layout.Columns(**layout_cfg),
    layout.MonadTall(**layout_cfg),
    layout.Max(),
]
