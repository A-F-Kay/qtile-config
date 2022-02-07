from libqtile import layout


layout_cfg = {
    'margin': 8,
    'margin_on_single': 15,
    'border_focus': '#F1D9FF',
    'border_normal': '#49453c',
    'border_width': 2,
    'border_on_single': True,
}

layouts = [
    layout.Columns(**layout_cfg),
    layout.Tile(**layout_cfg),
    layout.Max(),
]
