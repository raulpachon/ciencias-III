.model small 
.stack 
.data
    mensaje db 10,13,7, '--------Numero factorial--------- ','$'
    msIni db 10,13,7, 'Ingrese el numero -> ','$'
    msRes db 10,13,7, "El factorial es -> ","$"
    res db 1 ; entero de 8 bits sin signo
    num db ?
.code 

programa:

    mov ax, seg @data ; registro de datos, puente para acceso de datos
    mov ds, ax ; registro de segmento de datos

    ; muestro el mensaje de entrada
    mov ah, 09h 
    lea dx,mensaje
    int 21h
    
    
    mov ah, 09h 
    lea dx,msIni
    int 21h
    
    ;Capturo el numero hasta un salto de linea
    mov ah,01h
    int 21h
    sub al, 30h
    mov num,al
    
    ;Muestro el resultado
    mov ah,09h
    lea dx,msRes
    int 21h
    
    mov cl,num
    
    ciclo:
        mov al, res
        mov bl, cl
        mul bl
        mov res, al
    loop ciclo
    
    ;Imprimo el primero numero
    mov al,res
    AAM; desempaquetar
    mov bx, ax
    mov ah, 02h
    mov dl, bh
    add dl, 30h
    int 21h
    
    ;Imprimo el segundo numero
    mov ah, 02h
    mov dl, bl
    add dl, 30h
    int 21h
    
    
    .exit
    end programa
ret