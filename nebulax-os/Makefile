all: nebulax.bin

nebulax.bin: boot.asm
	nasm -f bin boot.asm -o nebulax.bin

run: nebulax.bin
	qemu-system-x86_64 -drive format=raw,file=nebulax.bin

clean:
	rm -f nebulax.bin
