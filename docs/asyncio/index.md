# ASYNCIO

## Awaitables

```python
{{include("asyncio_cook/co2.py")}}
```

## Coroutines
function that can be awaitable  
- coroutine function: an `async` function  
- coroutine object: return by coroutine function  

```python
{{include("asyncio_cook/co2a.py")}}
```

### Result
```
[INFO] 2021-12-21 05:56:33,703 <class 'coroutine'>
[INFO] 2021-12-21 05:56:34,704 hello coroutine
```

## Task
Tasks are used to scheduler coroutines concurrently

```python
{{include("asyncio_cook/co3.py")}}
```

## Waiting
[Waiting Primitive](https://docs.python.org/3.8/library/asyncio-task.html#id9
)
## References
- [Python reference](https://docs.python.org/3.8/library/asyncio-task.html)
- [A Hitchhikers Guide to Asynchronous Programming](https://github.com/crazyguitar/pysheeet/blob/master/docs/appendix/python-concurrent.rst)
- [Python asyncio](https://bbc.github.io/cloudfit-public-docs/)