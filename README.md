# Readme
A simple, keyword based, custom wordlist generator, which work by python. The interactive script will show you the way to make it work. It will generate tons of passwords about given keywords, with combining them with itselfs, numbers, special chars and etc.

```
Attention!

Script will not sort or remove duplicates of generated wordlist, this feature will be supplied later^^
```
 
### Prerequisites

Python v3 is enough.

```
# apt-get install python3
```

## Usage

Just run the script with Python3, and follow the interactive commands. When it starts, it will generate your text(wordlist) file named >>

```
wordList.txt
```
You can intercept process while it building your wordlist, it will stop the operation there, but your list will no be deleated.

Usage commands;

```
# cd customWordlistGenerator
# python wordlistGenerator.py
```

## Example

When you run the script, with keywords "github", "kaan" and "repo", it will generate words most likely passwords like;
(github is the most important one - script will explain you what that is)
```

Tgithub48T
!!!!Github!!!!22
repoQ85
githubrepo71C
...
With theese keywords, it will generate 81,046,746 combined word.

```

## License

MIT License

Copyright (c) 2019 Kaan Tekiner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
