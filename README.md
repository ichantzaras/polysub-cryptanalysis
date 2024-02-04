<h1 align="center">
polysub-cryptanalysis 
</h1>

Examples of applying [Kasiski examination](https://en.wikipedia.org/wiki/Kasiski_examination) and [Index of Coincidence](https://en.wikipedia.org/wiki/Index_of_coincidence) along with [Frequency analysis](https://en.wikipedia.org/wiki/Frequency_analysis) to restore cryptographic key of Vigenere encypted ciphertext and decrypt it.

Encrypted File
-------------
```
encrypted/hostiletext.txt
```

Structure
-------------

  - kasiski.py        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; kasiski examination related methods
  - ic.py             &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Index of coincidence related methods 
  - freq_analysis.py  &nbsp; &nbsp; frequency analysis related methods
  - processing.py     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; text transformation/processing related methods
  - const.py          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; constants
  - attack.py         &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; actual decryption 
