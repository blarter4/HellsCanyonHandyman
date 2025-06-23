"""Minimal Starlight interpreter prototype for NebulaX.
This is not a full implementation. It simply executes events defined
as dictionaries for demonstration purposes.
"""
import sys

# Simple parser for the prototype: lines of the form 'name <- event { ... }'
# We only handle the display command.

def parse(source):
    events = {}
    name = None
    for line in source.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if '<- event' in line:
            name = line.split('<-')[0].strip()
            events[name] = []
        elif line == '}':
            name = None
        elif name is not None:
            if line.startswith('display(') and line.endswith(')'):
                msg = line[len('display('):-1].strip('"')
                events[name].append(('display', msg))
    return events


def run(events):
    # In NebulaX each event would run when its inputs are ready.
    # Here we just execute in definition order.
    for name, actions in events.items():
        for action, value in actions:
            if action == 'display':
                print(value)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: starlight.py <file>')
        sys.exit(1)
    with open(sys.argv[1]) as f:
        source = f.read()
    events = parse(source)
    run(events)
