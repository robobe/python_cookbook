## Call Task from other thread
- Scheduler Task from other thread


```python linenums="1" hl_lines="12" title="task_from_thread.py"
{{include("asyncio_cook/call_and_execute/task_from_thread.py")}}
```

!!! Example "Result"
    ```
    [INFO] 2022-01-08 21:04:30,885 start from event loop
    [INFO] 2022-01-08 21:04:30,885 start from thread
    [INFO] 2022-01-08 21:04:31,886 done event loop
    [INFO] 2022-01-08 21:04:31,887 done thread
    ```

---

## Schedule 
```python linenums="1" hl_lines="14" title="schedule_fom_thread.py"
{{include("asyncio_cook/call_and_execute/schedule_fom_thread.py")}}
```

---

## Executer

```python linenums="1" title="executer.py"
{{include("asyncio_cook/call_and_execute/executer.py")}}
```
