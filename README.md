
# Insurance Medical Cost API

With this API users can use a machine learning model to predict the cost billed by medicial insurance dependent on certain characteristics of a person. This model takes the input variables Age, Gender, BMI and Smoker. 


## Input Variables

| Variables             | Options                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Age | 0-100 |
| Gender | 0 = Female, 1 = Male |
| BMI | 12-60 |
| Smoker | 0 = Nonsmoker, 1 = Smoker |


## API Reference

#### Get Medical Cost

```http
  GET /
```

| Type     | Example                |
| :------- | :------------------------- |
| `raw JSON`  | {"age": 50,"sex":0,"bmi":20,"smoker":0}|

