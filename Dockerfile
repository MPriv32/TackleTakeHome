FROM amazon/aws-lambda-python:3.8

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

#Copy and install requirements
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt

ARG GITHUB_ACCESS_TOKEN
ARG TABLE_NAME

ENV GITHUB_ACCESS_TOKEN $GITHUB_ACCESS_TOKEN
ENV TABLE_NAME $TABLE_NAME

# Set the CMD to the handler 
CMD [ "app.handler" ]