Some **regexp** operators covered in the homework reading (like `\d`) are part of **"Perl"** regexp.

`grep` won't recognize these unless you use the `-P` tag.

So, e.g., do:

&nbsp;`grep -P '\d' AIS.csv` - to find rows with digits

