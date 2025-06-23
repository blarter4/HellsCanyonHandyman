org 0x7c00

; Bootloader for NebulaX minimal demo

mov ax, 0x07c0
mov ds, ax
mov si, msg

print:
    lodsb
    or al, al
    jz done
    mov ah, 0x0e
    mov bx, 0x0007
    int 0x10
    jmp print

done:
    cli
    hlt

msg db 'NebulaX booted successfully!', 0

; Pad remainder of boot sector
 times 510-($-$$) db 0
 dw 0xaa55
