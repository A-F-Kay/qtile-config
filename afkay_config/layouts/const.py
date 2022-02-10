from libqtile import layout


layout_cfg = {
    'margin': 4,
    'margin_on_single': 8,
    'border_focus': '#F1D9FF',
    'border_normal': '#49453c',
    'border_width': 2,
    'border_on_single': True,
}

layouts = [
    layout.Columns(**layout_cfg),
    layout.Max(),
]
