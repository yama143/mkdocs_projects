# Random

A bunch of stuff to help me remember how to do things in mkdocs-material.

## Abbreviations
-------------------

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium

## Admonitions
---------------

!!! note

    I'm a note annotation.

??? note

    I'm a collapsable note annotation!


## Annotations
----------------
Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
{ .annotate }

1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be expressed in Markdown.


## Buttons
-----------
[DO NOT PUSH THIS DEFAULT BUTTON](#){ .md-button }

[DO NOT PUSH THIS PRIMARY BUTTON](#){ .md-button .md-button--primary }

[:fontawesome-solid-paper-plane: DO NOT PUSH THIS ICON BUTTON ](#){ .md-button .md-button--primary }


## Code Blocks
----------------
### default
``` py
from rich import inspect
```
### with title
``` py title="now with a title!"
from rich import inspect
```

### with linenums
``` py title="now with linenums!" linenums="1"
from rich import inspect

list1 = ['thing1', 'thing2', 'thing3']
inspect(list1, all=True)
```
### with highlights
``` py title="now with highlights!" linenums="1" hl_lines="4"
from rich import inspect

list1 = ['thing1', 'thing2', 'thing3']
inspect(list1, all=True)
```
### in-line 
The `#!python range()` function is used to generate a sequence of numbers.

## Tables
----------
### default
| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |


### right-aligned
| Method      | Description                          |
| ----------: | -----------------------------------: |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

### right-and-left-aligned
| Method      | Description                          |
| ----------: | :----------------------------------- |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

### sortable?
| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

## Lists
--------
### unordered
- Nulla et rhoncus turpis. Mauris ultricies elementum leo. Duis efficitur
  accumsan nibh eu mattis. Vivamus tempus velit eros, porttitor placerat nibh
  lacinia sed. Aenean in finibus diam.

    * Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
    * Nam vulputate tincidunt fringilla.
    * Nullam dignissim ultrices urna non auctor.

### ordered
1.  Vivamus id mi enim. Integer id turpis sapien. Ut condimentum lobortis
    sagittis. Aliquam purus tellus, faucibus eget urna at, iaculis venenatis
    nulla. Vivamus a pharetra leo.

    1.  Vivamus venenatis porttitor tortor sit amet rutrum. Pellentesque aliquet
        quam enim, eu volutpat urna rutrum a. Nam vehicula nunc mauris, a
        ultricies libero efficitur sed.

    2.  Morbi eget dapibus felis. Vivamus venenatis porttitor tortor sit amet
        rutrum. Pellentesque aliquet quam enim, eu volutpat urna rutrum a.

        1.  Mauris dictum mi lacus
        2.  Ut sit amet placerat ante
        3.  Suspendisse ac eros arcu
