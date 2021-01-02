from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class {{ table.class}}(BaseModel):
    {% for col in table.columns %}{{col}}: {{ table.datatypes[loop.index-1]}}
    {% endfor %}

    {% for col in table.columns %}{{col}}: {{ table.datatypes[loop.index-1]}}
    {% endfor %}
