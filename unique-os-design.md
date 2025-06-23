# NebulaX: A Unique Operating System Concept

NebulaX is a research operating system built entirely from first principles. It does not reuse existing OS concepts. Everything from hardware management to user experience is reinvented.

## Core Ideas

- **Quantum Event Kernel**: Instead of processes and threads, NebulaX uses "quantum events," ephemeral execution units that activate only when their dependencies are satisfied. Scheduling is event-driven rather than time-sliced.
- **Spatial Memory Fabric**: Memory is addressed by coordinates rather than linear addresses. The kernel tracks clusters of memory tiles, allowing programs to allocate memory in 3‑D space.
- **Protocol-Free I/O**: Drivers expose raw hardware capabilities. Applications negotiate their own data formats and semantics directly with the driver API.

## Starlight Language

NebulaX applications are written in Starlight, a domain-specific language designed for the quantum event model.

```
# sample.stl - a Starlight snippet
start <- event {
    display("Hello from NebulaX")
}
```

The syntax uses `<-` to define events. Each event executes once its inputs are ready. There is no global state; all data flows through events.

The prototype interpreter supports a `display` command for output and a simple `calc` command for arithmetic evaluation.

## Polychrome GUI

NebulaX comes with Polychrome, a graphical shell where windows are arranged on translucent layers in 3‑D space. Users navigate by rotating the workspace and placing applications on different spatial planes.

## Additional Components

- **Quantum File Orchestrator** – a file system that stores objects by entangled identifier rather than path
- **Event Graph Debugger** – visualizes event dependencies in real time
- **Crystalline Security Layer** – capability-based permissions enforced by hardware keys


## Boot Demo

A minimal boot sector is included under `nebulax-os/`. It prints a welcome message using BIOS services. Build it with `make` and run with `make run` using QEMU.
