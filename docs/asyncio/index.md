# ASYNCIO

## Awaitables

```python
{{include("asyncio_cook/co2.py")}}
```

## Coroutines
function that can be awaitable  
- **coroutine function**: define as `async` function  `async def f()` the call to async function return coroutine object  
- **awaitable**: anything that works with `await`: coroutine, Tasks, Futures  
- **coroutine object**: return by coroutine function  

```python
{{include("asyncio_cook/co2a.py")}}
```

### Result
```
[INFO] 2021-12-21 05:56:33,703 <class 'coroutine'>
[INFO] 2021-12-21 05:56:34,704 hello coroutine
```

## Task
Tasks wrap coroutine and used to scheduler coroutines concurrently


```python
{{include("asyncio_cook/co3.py")}}
```

## Waiting
### wait 
Wait method take list of tasks as iterable and return tow sets:  
- list of done/finished tasks  
- list of pending/unfinished tasks

```python
done, pending = await asyncio.wait([task_f, task_g])
```
### Wait for first task to finish it's work
```python
{{include("asyncio_cook/wait.py")}}
```

### wait with timeout
```python
{{include("asyncio_cook/wait_with_timeout.py")}}
```

### wait_for

```python
{{include("asyncio_cook/wait_for_demo.py")}}
```

## References
- [Python reference](https://docs.python.org/3.8/library/asyncio-task.html)
- [A Hitchhikers Guide to Asynchronous Programming](https://github.com/crazyguitar/pysheeet/blob/master/docs/appendix/python-concurrent.rst)
- [Python asyncio](https://bbc.github.io/cloudfit-public-docs/)
- [Guide to Concurrency in Python with Asyncio](https://www.integralist.co.uk/posts/python-asyncio/#theme)