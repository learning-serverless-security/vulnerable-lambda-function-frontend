```
USERNAME=learning-serverless-security
REPO=vulnerable-lambda-function-frontend

git clone https://github.com/$USERNAME/$REPO.git

cd vulnerable-lambda-function-frontend
```

```
FUNCTION_URL="<SPECIFY LAMBDA FUNCTION URL>"

sed -i "s|<INSERT FUNCTION URL HERE>|$FUNCTION_URL|g" index.html
```
