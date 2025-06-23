# NebulaX OS Demo

This repository contains a minimal bootable example of the **NebulaX** operating system concept. The demo is a 512-byte boot sector that simply prints a message using BIOS services. It can be run with QEMU on Windows or Linux. A project website is included via the `index.html` GitHub Pages site.

## Building

1. Install [NASM](https://www.nasm.us/) and [QEMU](https://www.qemu.org/).
2. Open a terminal in the `nebulax-os` directory.
3. Run:

```bash
make
```

This assembles `boot.asm` into `nebulax.bin`.

## Running in QEMU

Run the following from the `nebulax-os` directory:

```bash
make run
```

You should see a window displaying `NebulaX booted successfully!`.

## Files

- `nebulax-os/boot.asm` – assembly source for the boot sector
- `nebulax-os/Makefile` – build and run commands
 - `starlight.py` – prototype interpreter for the Starlight language
 - `hello.stl` – example Starlight script demonstrating display and `calc` commands

The boot demo is intentionally small and does not yet implement the full NebulaX kernel concepts, but it demonstrates how the project can start from first principles.
