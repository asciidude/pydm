<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/p8WIXrd.png" alt="Project logo"></a>
</p>

<h3 align="center">pydm</h3>

<div align="center">

<!-- [![Status](https://img.shields.io/badge/status-inactive-red.svg)]() -->
[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/asciidude/pydm)](https://github.com/asciidude/pydm/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/asciidude/pydm)](https://github.com/asciidude/pydm/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> pydm is a download manager created in Python. This is <b>under active development</b>.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)
- [License](./LICENSE)

## 🧐 About <a name = "about"></a>

pydm is a download manager, there are two variations, the CLI and GUI version, both of which are changeable through startup command. If you run the build (.exe) file, it will automatically start as GUI. See more in [Getting Started](#getting_started)

## 🏁 Getting Started <a name = "getting_started"></a>

```bash
# <param.> = Required, (type) = Type of param.

# Install Requirements
$ py -m pip install -r src/requirements.txt

# Run project (arguments provided ARE positional)
$ py src/pydm.py [-h] <gui> (bool) <link> (string) <name> (string)

# All other options other than cli/gui are CLI only
# You can also run the projects by /builds/pydm-xxx.exe
# If you are running the GUI version, put "_" for the link and name arguments
```

## ⛏️ Built Using <a name = "built_using"></a>

- [Python v3.9.6](https://python.org/en/) - The programming language used
- [Requests](https://pypi.org/project/requests/) - A library for creating requests
- [clint](https://pypi.org/project/clint/) - A library with pre-built functions for CLIs
- [argparse](https://pypi.org/project/argparse/) - A library for creating CLIs
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - A library for creating GUIs

## ✍️ Authors <a name = "authors"></a>

- [@asciidude](https://github.com/asciidude) - Idea & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- [@codic12](https://github.com/codic12) - codic has been making a window manager, oddly it inspired me to create a download manager

<i>💡 Fun fact, you pronounce "pydm" like pie-dim</i>