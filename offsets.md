# Calcolo offset

## Offset variabile - variabile

Questa è una funzione su ghidra; se vediamo che la funzione, all'interno, fa `gets(local_54)`,
e dobbiamo sovrascrivere `local_14`, allora per capire quanti byte dobbiamo scrivere basta
guardare gli offset delle variabili nello stack (`Stack[-0x14]`), e fare la differenza. Per esempio,
in questo caso dobbiamo (-0x54) - (-0x14) = -0x40, quindi dobbiamo scrivere 0x40 = 64 byte di
padding, e dopo la nostra payload.

```
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined main()
             undefined         AL:1           <RETURN>
             undefined1        Stack[-0x14]:1 local_14                                XREF[1]:     08048547(*)  
             undefined1        Stack[-0x54]:1 local_54                                XREF[1]:     0804852b(*)  
             undefined4        Stack[-0x64]:4 local_64                                XREF[1]:     080484ff(W)  
             undefined4        Stack[-0x68]:4 local_68                                XREF[2]:     08048507(W), 
                                                                                                   08048537(W)  
             undefined4        Stack[-0x6c]:4 local_6c                                XREF[2]:     0804850f(W), 
                                                                                                   0804853f(W)  
             undefined4        Stack[-0x70]:4 local_70                                XREF[6]:     08048517(*), 
                                                                                                   0804851f(*), 
                                                                                                   0804852f(*), 
                                                                                                   0804854b(*), 
                                                                                                   08048557(*), 
                                                                                                   0804856a(*)  
                             main                                            XREF[4]:     Entry Point(*), 
                                                                                          _start:080483f7(*), 0804867c, 
                                                                                          080486f8(*)  
```

## Offset variabile - return address

Se, sempre nella funzione di prima, vogliamo sovrascrivere il return address, ci basta fare
`Tasto destro sulla funzione > Function > Edit stack frame` e notare che l'offset del return
address è 0. Quindi, la differenza tra local_54 e retaddr è di 0x54, quindi ci basta scrivere
0x54 byte di padding, e dopo il return address.