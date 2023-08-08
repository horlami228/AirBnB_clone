#!/usr/bin/python3
from base_model import BaseModel

model1 = BaseModel()

print(model1.created_at)

import time
time.sleep(5)

print(model1.created_at)
model1.save
print(model1.updated_at)
