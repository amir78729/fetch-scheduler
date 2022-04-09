
<div align="center">
  
# Fetch Scheduler
  
A simple Python program that calls an API every five minutes in order to check if it's down
 
</div>

## Installing Libraries

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required libraries:

### `schedule`

We used this library in order to call functions periodically.

```bash
pip install schedule
```
### `jdatetime`

We used this library to be able to get date-time information in the Jalali calendar.

```bash
pip install jdatetime
```

### `numpy`

We used numpy to ease array computation in python.

```bash
pip install numpy
```

### `matplotlib`

We used matplotlib to plot our data.

```bash
pip install matplotlib
```

## Main Tasks

### Api Call

Calling the API every five minutes in order to check if it's down

### Log Data

Logging Every hours Data inside a text file (`<DATE>.txt`).

Here is an example of file in 1401/01/17

```
[1401/01/17 00:00:00]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:01]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:02]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:03]:  total: 12  successful: 11 failed: 1
[1401/01/17 00:00:04]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:05]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:06]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:07]:  total: 12  successful: 10 failed: 2
[1401/01/17 00:00:08]:  total: 12  successful: 11 failed: 1
[1401/01/17 00:00:09]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:10]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:11]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:12]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:13]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:14]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:15]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:16]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:17]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:18]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:19]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:20]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:21]:  total: 12  successful: 12 failed: 0
[1401/01/17 00:00:22]:  total: 12  successful: 11 failed: 1
[1401/01/17 00:00:23]:  total: 12  successful: 12 failed: 0
```

### Plot Data

plotting data every day at 00:00 (in `<date>.png`).
Here is an example of this diagram in 1401/01/17

![image](https://user-images.githubusercontent.com/44297246/162222551-9fdeea75-fc00-4a0e-a1d4-29d797b76889.png)

