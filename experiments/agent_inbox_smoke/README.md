# Agent inbox smoke exercise

This standalone exercise was added for an owner-authorized live agent-inbox repair
experiment. It is separate from the course lessons and is not imported by them.
No credentials, network services, audio devices or third-party packages are needed.

`arithmetic_mean` should return the arithmetic mean of a nonempty tuple and reject
an empty tuple with `ValueError`. The initially committed implementation contains
an intentional arithmetic defect; the tests describe the desired behavior.

From the repository root:

```sh
python3 -m unittest discover -s experiments/agent_inbox_smoke -v
```

Keep changes for this experiment in this directory. Do not alter course examples
or weaken the expected results to make the tests pass.
