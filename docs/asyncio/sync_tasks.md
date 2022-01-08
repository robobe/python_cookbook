- Using lock
- Using Event


## Calling Tasks
```python title="simple_tasks.py" linenums="1"
{{include("asyncio_cook/sync_tasks/simple_tasks.py")}}
```

!!! Example "Result"
    ```
    [INFO] 2022-01-08 15:49:20,719 start hello1
    [INFO] 2022-01-08 15:49:20,719 start hello2
    [INFO] 2022-01-08 15:49:21,720 end hello1
    [INFO] 2022-01-08 15:49:21,720 end hello2
    ```

## Sync Tasks
- using `asyncio.lock`


```python title="sync_tasks.py" linenums="1" hl_lines="7 10"
{{include("asyncio_cook/sync_tasks/sync_tasks.py")}}
```

!!! Example "Result"
    ```
    [INFO] 2022-01-08 18:31:06,517 start hello1
    [INFO] 2022-01-08 18:31:07,518 end hello1
    [INFO] 2022-01-08 18:31:07,518 start hello2
    [INFO] 2022-01-08 18:31:08,520 end hello2
    ```
---

## Events 
### Event signal between tasks

```python title="signal_between_tasks.py" linenums="1" hl_lines="13 17 24"
{{include("asyncio_cook/sync_tasks/signal_between_tasks.py")}}
```

### Signal for other thread


```python title="signal_from_other_thread.py" linenums="1" hl_lines="3 12 15 21"
{{include("asyncio_cook/sync_tasks/signal_for_other_thread.py")}}
```

