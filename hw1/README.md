# HW01: Text Editor Tutorials

Name: Catherine Lukner  
Course: CSC221

## Vim

So my vim tutorial decided it was going to be in Polish...
All the lesson names match the English version. For example Lekcja 1.2 is the same as Lesson 1.2 as the English version.
No, I did not read all of this in Polish, I just looked up an English version and read that then did the exercises in my version. It might be more convienient to change my laptop into English but I am determined to learn Polish. 

#### Question 1: What is the configuration file for Vim? What are the minimal changes to this configuration to allow for syntax highlighting and tab management for Python?

The configuration file for Vim is the .virmrc located in the home directory. 

Minimal changes to this configuration files that could allow for syntax highlighting is:

syntax enable

To allow for the standard four spaces when you hit tab, add change to the configuration file:

set ts=4

#### Question 2: What is the best/most popular way to extentend Vim? Does Vim have a "plugin" system?

According to the author of the article "VIM and Python – A Match Made in Heaven" (https://realpython.com/vim-and-python-a-match-made-in-heaven/#vim-extensions), one of the best extension mangers (but not the only one) is Vundle. Vim does have a plugin system and allows excellent customization with many different plugins. 

Other popular extensions for Vim are:
1. NERDTree - filesystem explorer
2. Syntastic - highlights problems with syntax
3. EsayMotion - navigates within current file

#### Question 3: What are the most popular Vim extensions for Python development? Use your favorite search engine to find out more about how to use Vim to edit and work with Python code.

Some of the most popular Vim extensions for Python development are:
1. vim-pathogen - plugin management
2. ctrlp.vim - file mangement
3. python-mode - pleasurable python code writing (it has pretty much everything for python code writng)
4. NERDtree - filesystem explorer
5. powerline - statusline plugin


## Emacs

#### Question 1: What is the configuration file for Emacs? Find some example Emacs configuration files, especially ones that deal with Python development, and provide links to them. 

The configuration file for Emacs could be ~/.emacs, ~/.emacs.el, or ~/.emacs.d/init.el. Any of these names consistutes a valid config file. 
Some example Emacs configuration files are:
1. https://gist.github.com/nilsdeppe/7645c096d93b005458d97d6874a91ea9
2. https://gist.github.com/widdowquinn/987164746810f4e8b88402628b387d39 (The example is under the Install packes...Add the following to the init.el file)
3. https://gist.github.com/rplzzz/11258794


#### Question 2: What is the best/most popular way to extentend Emacs? Does Emacs have a "plugin" system?

Emacs does have a plugin system that allows Emacs to discover and load plugins. 
According to this Quora article, https://www.quora.com/What-are-some-must-have-Emacs-packages-and-modes-that-one-should-check-out-when-just-starting-out, and the  "What are the best plugins to increase productivity on Emacs" (http://xmodulo.com/best-plugins-to-increase-productivity-on-emacs.html) some of the popular ways to extend Emacs are:
1. IDO or HELM
2. Flyspell / Flycheck, or some other syntax/spell checking system
3. Avy, or another tool for moving around the buffer easily
4. Magit
5. A file manager (e.g. Dired+, SC)
6. Kill-ring enhancements like Popup-Killring
7. Auto-completion tools of some sort
8. Which-key or some other functionality discovery tool
9. Cutomization of Org-mode 
10. Terminal tools
11. Publishing tools (Auctex, bibtex, etc)
12. package management (e.g. use-package)
13. Appearance tweaks (powerline, etc)

#### Question 3: What are the most popular Emacs extensions for Python development? Use your favorite search engine to find out more about how to use Emacs to edit and work with Python code.

Some of the most popular Emacs extensions for Python development are:
1. Jedi.el - auto-completion package; aims at helping your Python coding in a non-destructive way; also helps you to find information about Python objects, such as docstring, function arguments and code location.
2. Projectile - project interaction library for Emacs; its goal is to provide a nice set of features operating on a project level without introducing external dependencies
