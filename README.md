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

```
BUCKET_NAME="serverless-static-website-$(date +%s)"
REGION="us-east-1"

aws s3 mb s3://$BUCKET_NAME --region $REGION
```

```
aws s3api put-public-access-block \
  --bucket "$BUCKET_NAME" \
  --public-access-block-configuration '{
    "BlockPublicAcls": false,
    "IgnorePublicAcls": false,
    "BlockPublicPolicy": false,
    "RestrictPublicBuckets": false
  }'
  
aws s3 cp index.html s3://$BUCKET_NAME/index.html

aws s3 website "s3://$BUCKET_NAME/" --index-document index.html
```
