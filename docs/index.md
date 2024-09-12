# Hypermedia

A fully typed Python HTML Renderer with a focus on composability of elements. A perfect pair for </>htmx and has FastAPI integration.
___


## Showcase


=== "python"

    ```python title="views/index.py"
    --8<-- "index/showcase.py:snippet"
    ```

    1. This function is usually placed in `commons.py` or similar since it will be used by all view files.


=== "index(user="John Doe").dump()"

    ```html hl_lines="10 14-17"
    <html>

    <head>
        <title>Welcome to test.com</title>
    </head>

    <body>
        <header>
            <!-- (1) -->
            <div>John Doe<button hx-get='/logout'>log out</button></div>
        </header>
        <main>
            <!-- (2) -->
            <div>
                <h1>Welcome</h1>
                <p>Lorem ipsum...</p>
            </div>
        </main>
        <footer></footer>
    </body>

    </html>
    ```

    1. Base was extended with result from `user_header(user: str)` function because a user was logged in!
    2. This part is rendered by the `partial()` function.

=== "partial().dump()"

    ```html
    <div>
        <h1>Welcome</h1>
        <p>Lorem ipsum...</p>
    </div>
    ```


## Why use Hypermedia

* You need to create html with Python


## Goal

## Why

## Features

## Contributing

Contributing section not written yet. but basically, add issues, ask good questions. Come with good suggestions <3

## Installation

Package is on pypi. Use `pip` or `poetry` to install

```sh
pip install hypermedia
```
```sh
poetry add hypermedia
```


what to do next? head over to the [quickstart](/quickstart) or [introduction](/introduction) sections!
