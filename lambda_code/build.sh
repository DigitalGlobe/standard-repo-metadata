# These commands create a zip file deployable to AWS Lambda

mkdir dist
pip install -r requirements.txt -t ./dist
cp grab.py dist/grab.py
cp lambda_handler.py dist/lambda_handler.py
cp yaml-schema.yml dist/yaml-schema.yml
cd dist
zip -r ../deploy.zip *
cd ..
