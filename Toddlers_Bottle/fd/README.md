## fd

This challenge focuses on the use of [file descriptors](https://en.wikipedia.org/wiki/File_descriptor).

We are given the following description/clues.

![Description](/Toddlers_Bottle/fd/Images/fd_description.png)

Upon connecting to we see a few files and their permissions.

![Files](/Toddlers_Bottle/fd/Images/files_and_permissions.png)

We don't have permission to open the flag file but we can look at the C file.

![C File](/Toddlers_Bottle/fd/Images/fd_c_file.png)

The first if statement just checks that we provide an argument to the program. Next we call the atoi function which converts a string to an integer and subtract 0x1234 from it. We then call the read function which will attempt to read up to 32 bytes from file descriptor fd into the buffer starting at buf. On success, the number of bytes read is returned (zero indicates end of file), and the file position is advanced by this number.

Lastly we call the negation of the strcmp function. The function compares the two strings "LETMEWIN\n" and buf. It returns an integer less than, equal to, or greater than zero if "LETMEWIN\n" is found, respectively, to be less than, to match, or to be greater than buf. If we can can successfully get the return value to be greater than zero then we should have our flag. Through testing on the negation of the strcmp function, one will find that the only way for this to be greater than zero is to have "LETMEWIN\n" and buf be equal to each other.


### Putting it all 
