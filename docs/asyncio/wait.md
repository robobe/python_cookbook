

## gather
Wait for multiple asynchronous tasks to complete

```python
{{include("asyncio_cook/wait_demos/wait_all.py")}}
```

!!! Example "Result"
    ```
    [INFO] 10:04:51 Run: 1 sec
    [INFO] 10:04:52 Run: 2 sec
    [INFO] 10:04:53 Run: 3 sec
    ```
---

## wait
[python.org](https://docs.python.org/3/library/asyncio-task.html#id9)  

- Wait for first Task to finished.
- `wait()` does not cancel the futures when a timeout occurs.

```python linenums="1" hl_lines="20"
{{include("asyncio_cook/wait_demos/wait_demo.py")}}
```

### wait timeout

```python linenums="1" hl_lines="20 22"
{{include("asyncio_cook/wait_demos/wait_with_timeout.py")}}
```

!!! Example "Result"
    ```
    [INFO] 2022-01-08 11:34:43,555 hello2
    [INFO] 2022-01-08 11:34:43,555 hello1
    ```

---

## wait_for
- Wait for the awaitable to complete with a timeout.
- If timeout raise Task are cancelled

```python linenums="1" hl_lines="20" title="wait_for_demo.py"
{{include("asyncio_cook/wait_demos/wait_for_demo.py")}}
```

!!! note
    Task cancel if time out raise  
    To protect task from cancelling use `asyncio.shield`  
    Replace line 17 with
    ```
    await asyncio.wait_for(asyncio.shield(task), timeout=1)
    ```

!!! Example "Without shield"
    ```
    [INFO] 09:59:20 start work 2
    [ERROR] 09:59:21 oops Timeout
    ```

!!! Example "With shield"
    ```
    [INFO] 10:00:05 start work 2
    [ERROR] 10:00:06 oops Timeout
    [INFO] 10:00:07 end work 2
    ```


## Other examples
- Run task multiple time with timeout until complete 
  
```python title="wait_until_success.py"
{{include("asyncio_cook/wait_demos/wait_until_success.py")}}
```


