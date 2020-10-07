Lambda function - 
Read json S3 files and check the output in cloudWatch logs.

- Create a lambda function with this code.
- Create a S3 bucket and configure this event to send results to cloud watch as below: 
    > event with PUT request
    > select the above created lambda function in SEND TO.
- Upload the test json files to S3 bucket and check the logs.

