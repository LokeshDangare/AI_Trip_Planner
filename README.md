### Commands for running the project

#### Run in command prompt
``` 
uv --version 
```

```
import shutil
print(shutil.which("uv"))
```

```
pip install uv
```

```
uv init AI_Trip_Planner
```

```
uv pip list
```

```
uv python list
```

```
uv python install cpython-3.10.18-windows-x86_64-none (Select any from list to download and install)
```

``` 
uv python list
```

##### if you have conda activate, then first deactivate
```
conda deactivate
```

##### Create a virtual environment
```
uv venv trip --python cpython-3.10.18-windows-x86_64-none
```

##### Activate the uv environment in cmd
```
Go to trip --> Go to Script --> Copy the path of activate.bat --> paste it to cmd terminal --> Enter
```

##### Install the packages
```
uv pip install langchain
```

##### Install the requirements
```
uv pip install -r requirements.txt
```

To load a main.py file, Execute below command in seperate cmd terminal before running streamlit_app.py file
```
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
``` 

