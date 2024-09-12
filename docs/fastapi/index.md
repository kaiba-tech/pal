# Hypermedia and FastAPI

Hypermedia can be used with any framework, but was created with FastAPI in mind and thus ships with some utility functions.

In FastAPI you create function and decorate them to create routes. When FastAPI gets a request it looks for a function that is decorated with a path that matches the url. 

This section assumes you have read the [html](/html) section of the documentation.


## Returning html in FastAPI



```python
from fastapi import FastAPI
from hypermedia import Div

app = FastAPI()

@app.get("", response_class=HTMLResponse)
async def index(request: Request) -> None:
    """Return an index page."""
    return Div("Hello world").dump()

```

This is all you have to do. open `localhost:port` in your browser and you should get a page with the text `Hello world`.

Notice the `.dump()`

with @htmx decorator

```python
@app.get("", response_class=HTMLResponse)
@htmx
async def index(
    request: Request,
    partial: Element = Depends(render_simple_flows_index_partial),
    full: Element = Depends(full(render_simple_flows_index)),
) -> None:
    """Return the list of transformers."""
    pass


```
