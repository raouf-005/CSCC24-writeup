## Solution to ret2win with lack of gadgets

### First Solution:

I opted for crafting shellcode to pass the arguments.
By satisfying the condition through the shellcode, 
I managed to overcome the challenge's requirement. However, there was a hurdle:
I didn't have the buffer address or any gadget to leak information. 
After debugging, I observed that `rdi` contains an address after the first `ret`. Leveraging this, 
I leaked the address and calculated the buffer's address by adding 10 bytes to it.
Then, I redirected the flow to the `ret2win` function, effectively achieving the desired outcome.

### Second Solution:

Another approach I considered was bypassing the condition that checks for the two arguments. 
If successful, I could directly jump to the `ret2win` function without setting up the arguments explicitly. 
This strategy involves understanding how the argument check is implemented and finding a way to circumvent it.
