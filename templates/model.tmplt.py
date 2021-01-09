from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class {{ table.class}}(BaseModel):
    {% for col in table.column_details %}{{col['column_name']}}: {{ col['pydantic_type']}}
    {% endfor %}
