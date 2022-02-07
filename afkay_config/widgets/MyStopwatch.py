from datetime import datetime, timedelta

from libqtile.widget import base


class MyStopwatchState:
    Idle = 'idle'
    Running = 'running'
    Paused = 'paused'
    Stopped = 'stopped'


class MyStopwatch(base.InLoopPollText):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ('update_interval', 1.0, "Update interval in seconds"),
        ('format', "{status} {h} {m} {s}", "Stopwatch format"),
    ]

    def __init__(self, **config):
        super().__init__("", **config)
        self.add_defaults(base.PaddingMixin.defaults)
        self.add_defaults(base.MarginMixin.defaults)
        self.add_defaults(MyStopwatch.defaults)
        
        self.state = MyStopwatchState.Idle
        self.elapsed_time = 0
        
        self.add_callbacks({
            'Button1': self.on_lclick,
            'Button3': self.on_rclick,
        })
        
    def on_rclick(self):
        if self.state in [MyStopwatchState.Running, MyStopwatchState.Paused]:
            self.state = MyStopwatchState.Stopped
        elif self.state == MyStopwatchState.Stopped:
            self.state = MyStopwatchState.Idle
            self.elapsed_time = 0

    def on_lclick(self, *args, **kwargs):
        if self.state == MyStopwatchState.Idle:
            self.state = MyStopwatchState.Running
            self.elapsed_time = 0
        elif self.state == MyStopwatchState.Running:
            self.state = MyStopwatchState.Paused
        elif self.state in [MyStopwatchState.Paused, MyStopwatchState.Stopped]:
            self.state = MyStopwatchState.Running

    # FIXME: Quick clicks fastes elapsed time than it must be in real :)
    # Possible solution: make datetime.now() for 
    #   started time & stopped time + save elapsed seconds on pause and stop
    def poll(self, *args, **kwargs):
        fmt = self.format
        if self.state == MyStopwatchState.Idle:
            return "⏱️ " + self.state
        elif self.state == MyStopwatchState.Running:
            self.elapsed_time += 1
            status = "⏱️"
        elif self.state == MyStopwatchState.Paused:
            status = "⏸️"
        else: # .STOPPED
            status = "🛑"
            
        seconds = self.elapsed_time
            
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        variables = {
            'h': f'{hours}h' if hours > 0 else '',
            'm': f'{minutes}m',
            's': f'{seconds}s',
            'status': status
        }

        return fmt.format(**variables)

