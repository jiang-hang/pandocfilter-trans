# what is it ?

it is a pandoc filter witten in python to translate the markdown from english to chinese(or other language). 

Also it is a good template to do something else on the markdown file.

# what it does ?

it collects the words in Para/Plain/Strong/Emph/Header section, send them for translation, replace the original content with the translated one.

# how to use it ?

`pandoc aa.md --filter ./trans.py -t markdown -o aa_tr.md`

Note that , you need to use your own translation API for it. It is a fake translation call in the code, which makes the code runnable.

# More info

The blog in chinese is [here](http://www.bagualu.net/wordpress/archives/5340#%E7%AC%AC%E4%BA%8C%E4%B8%AAfilter%E8%8B%B1%E6%96%87%E7%BF%BB%E8%AF%91)

# License

MIT License

Copyright (c) 2016 Jiang-hang, http://www.bagualu.net

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
