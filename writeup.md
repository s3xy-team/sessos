# plz-patch-me

This is a simple challenge about, as the name implies, patching a binary.

## Flag

`spritz{th4ts_wh4t_sh3_s41d}`

## Solution

Upon opening the binary with Ghidra, we can see right away that the first check it does is something similar to this:
```c
gets(local_78);
iVar1 = strcmp(local_78,local_b8);
if (iVar1 != 0) {
        puts("Incorrect!");
        exit(0);
}
```

So, we can easily see that the `local_b8` variable represents a string. Thus, by assigning it the type `char[n]`
we can make Ghidra correctly show it to us as a string (After some trial and error, we can see that it's sufficient to set `n` to 64
all characters in local_b8 are correctly displayed by gdb).
Thus, this check can be passed just by inputting `Dwight Schrute, position Assistant to the regional manager`

---

The second check that the binary does is something similar to this:
```c
local_c0 = get_rand();
print_hobby();
scanf("%d",&local_c8);
if (local_c0 != local_c8) {
        puts("Not a nice hobby! You\'re fired!\n");
        exit(0);
}
```

Here, we can understand that we need to guess the random number. It is pretty low, only ranging from 0 to 5,
so it could be easily guessed just by running the binary a small amount of times, but let's patch it anyway :)

As with any patching challenge, there are multiple ways to approach this, my approach was to change the first
two instructions of the `get_rand` function to

```asm
xor rax, rax
ret
```

What the first instruction does, is zero out the register RAX (anything xorred with itself is equal to 0),
thus setting the return value to 0 (since it is, like almost always in the linux/x86 world, saved in the RAX register).
Then, we simply return from this function.

Given all of this, when we are asked about our favourite hobby, we can just say it's `0 - Eat`

---

At this point the challenge would be complete, but there are some loops in main that print many times the same
word, and sleep for one second at each iteration. Patching the call to `sleep(1)` to be a call to `sleep(0)` is easy,
and can be done by substituting the two `MOV EDI, 1` that are before the two `CALL <EXTERNAL>::sleep` to `MOV EDI, 0`.